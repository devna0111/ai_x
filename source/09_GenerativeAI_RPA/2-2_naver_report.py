# 파일 백업 후, 기존의 now_list 시트를 prev_list로 하고 now_list에 네이버 쇼핑목록 업데이트
from naverOpenai import get_naver_api_data, str_json_dataframe, get_openai_shopping_analysis, get__openai_news_summarize
import xlwings as xw
import handle_sheet as hs

def main() :
    # 1. genai_rap.xlsx 파일 열기
    file_path = "genai_rpa.xlsx"
    wb = xw.Book(file_path)

    # 2 ~ 4 함수 호출
    hs.handle_init_sheet(file_path,wb)

    # 5. 네이버 api 쇼핑목록 데이터 가져오기(json타입str -> dict -> DataFrame) 
    str_data = get_naver_api_data('shop','아깽이용품')
    df_data = str_json_dataframe(str_data)

    # 6. 'now_list' 시트에 df_data 내용을 A1 셀에 업데이트
    hs.update_nowlist(wb, df_data)

    # 7. 분석 보고서 업데이트
    # 쇼핑 목록 분석
    result_analysis = get_openai_shopping_analysis(wb)
    # 뉴스 분석
    str_news_data = get_naver_api_data('news','포켄스') # 뉴스 검색 목록
    result_summary = get__openai_news_summarize(str_news_data)
    # 'prev_report' 시트를 삭제, 'now_report' 복사 후 이름을 'prev_report'로, 분석글 now_report 업데이트, 일자 최신화
    hs.update_now_report(wb, result_analysis, result_summary)

    # 8. 파일 저장 후 닫기
    hs.save_close_file(file_path,wb)

if __name__ == '__main__' :
    main()
