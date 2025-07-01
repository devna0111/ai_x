# 파일 백업 후, 기존의 now_list 시트를 prev_list로 하고 now_list에 네이버 쇼핑목록 업데이트
from naverOpenai import get_naver_api_data, str_json_dataframe
import xlwings as xw
import handle_sheet as hs

def main() :
    # 1. genai_rap.xlsx 파일 열기
    file_path = "genai_rpa.xlsx"
    wb = xw.Book(file_path)

    # 2 ~ 4 함수 호출
    hs.handle_init_sheet(file_path,wb)

    # 5. 네이버 api 쇼핑목록 데이터 가져오기(json타입str -> dict -> DataFrame) 
    str_data = get_naver_api_data('shop','포켄스')
    df_data = str_json_dataframe(str_data)

    # 6. 'now_list' 시트에 df_data 내용을 A1 셀에 업데이트
    hs.update_nowlist(wb, df_data)

    # 7. 파일 저장 후 닫기
    hs.save_close_file(file_path,wb)

if __name__ == '__main__' :
    main()
