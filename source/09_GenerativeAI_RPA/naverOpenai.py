import os
import sys
import urllib.request
from dotenv import load_dotenv
from openai import OpenAI
import json
import pandas as pd

def get_naver_api_data(media, word) :
    '''
    네이버 오픈API 검색기능을 활용해 word에 대해 media 검색한 결과의 str을 return
    media = "shop" or "news" 
    '''
    load_dotenv()
    client_id = os.getenv('Client_ID')
    client_secret = os.getenv('Client_Secret')
    encText = urllib.parse.quote(word)
    # media = "news"
    url = f"https://openapi.naver.com/v1/search/{media}?display=20&sort=date&query={encText}" # JSON 결과
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        # data = json.loads(response_body.decode('utf-8'))
        # pd.DataFrame(data.get('items'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        pass

def str_json_dataframe(str_json_result) :
    """Json 스타일의 str을 DataFrame으로 return"""
    if isinstance(str_json_result, str) :
        json_result = json.loads(str_json_result)
        
    else :
        json_result = dict()
    # 딕셔너리 => DataFrame으로
    items = json_result.get("items",[])
    df = pd.DataFrame(items)
    df['순위'] = range(1, len(df)+1)
    df.set_index("순위", inplace=True)
    return df


def aiconn(prompt) :
    # prompt를 입력받아 LLM 요청 후 메세지 수신, 분석글을 return
    load_dotenv()
    client = OpenAI()
    completion = client.chat.completions.create(
        model = 'gpt-4.1-nano',
        messages = [{'role':'user', 'content' : prompt}],
        # max_tokens=300,
    )
    # 분석글 리턴
    return completion.choices[0].message.content

def get_openai_shopping_analysis(wb) :
    # 2. prev_list, now_list 시트 전체 내용 불러오기
    prev_sheet = wb.sheets['prev_list']
    now_sheet = wb.sheets['now_list']
    prev_data = prev_sheet.used_range.value # 사용된 범위의 데이터
    now_data = now_sheet.used_range.value
    
    # 3. 프롬프트 작성
    prompt = f"""다음 두 목록을 비교분석하여 prev_list목록에서 now_list목록으로 바뀐 주요 특징을 추출해줘.
    prev_list 목록 : {prev_data}
    now_list 목록 : {now_data}
    비교분석 결과를 바탕으로 구체적인 수치, 상품명, 쇼핑몰 명 등을 언급해서 한글로 100자 이내로 분석글을 작성해줘"""
    return aiconn(prompt=prompt)

def get__openai_news_summarize(str_news_data) :
    # 뉴스 요약 return
    prompt = f""" 다음 뉴스 내용을 구체적인 수치, 고유명사를 언급하며 글머리를 활용하여
    한글 200자 이내로 요약 글을 작성해 줘.
    뉴스내용 {str_news_data}
    """
    return aiconn(prompt=prompt)