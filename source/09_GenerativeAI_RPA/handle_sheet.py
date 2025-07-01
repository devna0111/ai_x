import datetime
import shutil # 파일 및 디렉토리 작업 도와주는 lib
import xlwings as xw
import os

def handle_init_sheet(file_path, wb) :
    # 2. 백업(파일명 : genai_rpa2507011258.xlsx)
    timestamp = datetime.datetime.now().strftime("%y%m%d%H%M")
    backupfilename = f"genai_rpa{timestamp}.xlsx"
    shutil.copy(file_path,backupfilename)
    print("백업 파일 생성 완료",backupfilename)
    # 3. 'prev_list' 시트를 삭제
    sheet_names = [s.name for s in wb.sheets]
    if 'prev_list' in sheet_names :
        wb.sheets['prev_list'].delete()
        print("prev_list 시트 삭제 완료")
    else :
        print("prev_list 시트가 존재 하지 않아 삭제하지 못함")
    # 4. 'now_list' 시트를 복사하고 그 이름을 'prev_list'로 수정
    if 'now_list' in sheet_names :
        now_sheet = wb.sheets['now_list']
        prev_sheet = now_sheet.copy(after=now_sheet) # 깊은복사
        prev_sheet.name = "prev_list"
        print("now_list 시트를 prev_list 시트로 복사 완료")
    else :
        print("now_list 시트가 존재하지 않아 작업 중단")
        return

def update_nowlist(wb, df_data) :
    # 6. 'now_list' 시트에 df_data 내용을 A1 셀에 업데이트
    now_sheet = wb.sheets['now_list']
    now_sheet.clear()
    now_sheet.range('A1').value = df_data
    print("now_list 업데이트 완료")

def save_close_file(file_path, wb) :
    wb.save(file_path)
    wb.close()
    print('workbook 저장 및 닫기 완료')

def update_now_report(wb, result_analysis, result_summary) :
    ''' 쇼핑 검색 결과와 뉴스 검색 결과를 업데이트 하고 일시를 최신화 하는 함수
    wb : 열려있는 엑셀 운용 객체, result_analysis : 쇼핑 검색 결과, result_summary : 뉴스 요약 결과
    ''' 
    # prev_report 삭제
    sheets_name = [s.name for s in wb.sheets]
    if 'prev_report' in sheets_name :
        wb.sheets['prev_report'].delete()
        print("prev_report 시트 삭제")
    else :
        print("해당 하는 시트가 없습니다.")
    
    if 'now_report' in sheets_name :
        now_sheet = wb.sheets['now_report']
        prev_sheet = now_sheet.copy(after=now_sheet)
        prev_sheet.name = 'prev_report'
        print('prev_report 시트 복사 완료')
    else :
        now_sheet = wb.sheets['origin_report'].copy(after=wb.sheets['origin_report'])
        now_sheet.name = 'now_report'

    # 분석글 업데이트
    current_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now_sheet.range('A3').value = current_dt + " 기준" # 오른쪽 정렬
    # now_sheet.range('A3').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
    now_sheet.range('A5').value = result_analysis
    now_sheet.range('A5').api.WrapText = True # 내용이 셀보다 길면 자동 줄바꿈 활성화
    now_sheet.range('A8').value = result_summary
    now_sheet.range('A8').api.WrapText = True # 내용이 셀보다 길면 자동 줄바꿈 활성화
    # now_sheet를 pdf파일로 생성 => genai_rpa_2507011655.pdf
    timestamp = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    file_name = f'genai_rpa_{timestamp}.pdf'
    file_path=os.path.join(os.getcwd(),file_name)
    now_sheet.api.ExportAsFixedFormat(0, file_path)
    print("pdf파일 저장완료",file_name)