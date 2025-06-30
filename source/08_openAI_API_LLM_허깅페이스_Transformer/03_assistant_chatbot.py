# 자동완성이 안 될 경우 가상환경 설정을 체크 : ctrl + shift + p => select interpretter => 가상환경 선택
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os
import time
import warnings
# 0. warning 무시
warnings.filterwarnings("ignore")

# 1. client 객체 생성
load_dotenv(override=True)
client = OpenAI()

# 2. assistant 객체 생성
assistant = client.beta.assistants.create(
    name = "HelpKitty",
    instructions = '당신은 유능한 고양이 양육 전문가입니다. 사용자 질문에 20글자 이내로 친절하게 답변하세요',
    model = 'gpt-4o-mini',
#     tools=
)

# 3. thread 객체 생성
thread = client.beta.threads.create()

print('챗봇이 활성화 됩니다. 모든 대화 이력은 저장됩니다.')
print("만약 '끝','종료','bye','exit' 라고 하시면 상담이 종료됩니다")

while True :
    user = input("아깽이 양육에 관한 걸 질문하세요! : ")
    if user in ['끝','종료','bye','exit',"'끝'","'종료'","'bye'","'exit'"] :
        print('HelpKitty가 종료됩니다. 이용해주셔서 감사합니다.')
        for i in range(3) :
            print(f"{i+1}...",end='')
            time.sleep(1)
        print('Bye')
        break
    # 4 ~ 6. user를 thread에 추가하고 실행한 후 최종 답변을 출력
    client.beta.threads.messages.create(
        thread_id = thread.id,
        role = 'user',
        content = user
    )
    # 5. run 실행
    client.beta.threads.runs.create_and_poll(
        assistant_id=assistant.id,
        thread_id=thread.id
    )
    # 6. 최종 assistant 답변 출력
    messages = client.beta.threads.messages.list(thread_id=thread.id).data
    assistant_reply = messages[0]
    reply_text = assistant_reply.content[0].text.value
    # print("user :",user)
    print("assistant :",reply_text)

# 7. 대화 이력 뽑기
messages_list = sorted(client.beta.threads.messages.list(thread_id=thread.id),key=lambda x : x.created_at)
with open('data/ch7_chat_history.txt','w',encoding='utf-8') as f :
    for msg in messages_list :
        dateStyle = time.localtime(msg.created_at)
        # 보기좋은 문자열 형식으로 변환
        dateStyle_str = time.strftime('%Y-%m-%d %H:%M:%S',dateStyle)
        f.write(f"{msg.role:9}({dateStyle_str}) : {msg.content[0].text.value}\n")