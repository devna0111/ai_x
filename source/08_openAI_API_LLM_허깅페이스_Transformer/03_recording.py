import sounddevice as sd
from scipy.io.wavfile import write # mp3는 스트리밍이 안되어 wav로 스트리밍
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import os

fs = 16000 # 샘플레이트 16kHz
seconds = 5 # 음성 녹음 길이 5초

print('지금부터 5초간 녹음합니다')
recording = sd.rec(int(seconds*fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

file_name = "data/ch06_live_input.wav"
write(file_name, fs, recording)
print('녹음된 음성이 저장되었습니다.(크기 : {}byte)'.format(len(recording)))

# os.system(f'start {file_name}')  # 파일이 mp3여도 동작

# 저장된 녹음 파일을 whisper API로 전송, text로 받기
with open(file_name, 'rb') as file :
    load_dotenv()
    client = OpenAI()
    live_transcript = client.audio.transcriptions.create(
        file = file,
        model = 'whisper-1',
        response_format='text',
        language = 'ko',
    )
    
print('실시간 녹음 변환된 텍스트 : ', live_transcript)

summary = client.chat.completions.create(
    model = 'gpt-4.1-nano',
    messages=[
        {'role':'system','content':"넌 무엇이든지 3줄로 요약하는 요약쟁이야. 항상 한국어로 답변하지."},
        {'role':'user','content':live_transcript}],
    temperature=2,
    frequency_penalty=0
)

AI_message = client.audio.speech.create(
    input = summary.choices[0].message.content,
    model = 'whisper-1',
    voice='shimmer',
    speed=1,
    )

file_name = 'data/ch00_TEST.mp3'
with open(file_name,'wb') as file :
    file.write(AI_message)


os.system(f'start {file_name}')

# # 파일 삭제
# import os
# try : 
#     os.remove(file_name)
#     print(f"{file_name} file을 정상 삭제 하였습니다.")
# except Exception as e:
#     print("파일 삭제 중 오류 발생 :",e)