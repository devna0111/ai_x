import xlwings as xw
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

# 1. 엑셀 열기
file_path = "genai_rpa.xlsx"
wb = xw.Book(file_path)
# 2. prev_list, now_list 시트 전체 내용 불러오기
prev_sheet = wb.sheets['prev_list']
now_sheet = wb.sheets['now_list']
prev_data = prev_sheet.used_range.value # 사용된 범위의 데이터
now_data = now_sheet.used_range.value

print(prev_data, now_data)

# 3. 프롬프트 작성
prompt = f"""다음 두 목록을 비교분석하여 prev_list목록에서 now_list목록으로 바뀐 주요 특징을 추출해줘.
prev_list 목록 : {prev_data}
now_list 목록 : {now_data}
비교분석 결과를 바탕으로 구체적인 수치, 상품명, 쇼핑몰 명 등을 언급해서 한글로 100자 이내로 분석글을 작성해줘"""
# 4. LLM 요청 후 메세지 수신
load_dotenv()
client = OpenAI()
completion = client.chat.completions.create(
    model = 'gpt-4.1-nano',
    messages = [{'role':'user', 'content' : prompt}],
    # max_tokens=300,
)
# 5. 분석글 출력
print(completion.choices[0].message.content)
# print('-----------------------------------------------------------------')
# print(completion)