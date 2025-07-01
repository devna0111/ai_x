import xlwings as xw
import os
# 1. 파일 경로 설정(현재)
file_name = '1-1_xlwings_test.xlsx'
file_path = os.path.join(os.getcwd(), file_name)

print(file_path)

# 2. 엑셀 열기
wb = xw.Book(file_path)

# 3. sheet 선택
sheet = wb.sheets.active

# 4. B1과 B2의 값 연산
b1 = sheet.range('B1').value
b2 = sheet.range('B2').value
# 두 값의 차이 B3 셀에 기입
result = b1 - b2
sheet.range('B3').value = result
print('연산 결과 쓰기 완료')

# 5. 저장 및 닫기
wb.save()
wb.close()