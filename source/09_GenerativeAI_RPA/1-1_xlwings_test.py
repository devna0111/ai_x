import xlwings as xw

# 현재 열린 엑셀 파일의 활성화 된 sheet의 데이터 가져옴
wb = xw.apps.active.books.active
sheet = wb.sheets.active
print('데이터 가져와 연산 수행')

# B1과 B2의 값을 가져옵니다.
b1 = sheet.range('B1').value
b2 = sheet.range('B2').value
print(b1,b2)
# B1에서 B2를 뺀 값을 계산합니다.
result = b1 - b2
sheet.range('B3').value = result
print('연산 결과 쓰기 완료')