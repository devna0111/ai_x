from predict import loaded_model, predict_apt_price
import xlwings as xw

def main() :
    "Excel 파일을 열고 데이터를 가져와 예측한 결과를 저장 후 파일 닫기"
    file_path = "../data/ex3_xlwing.xlsx"
    wb = xw.Book(file_path)
    ws = wb.sheets.active
    # 엑셀 데이터를 읽어서 predict하고 결과를 E열에 넣기
    for line in range(2,5) :
        year = ws.range(f'B{line}').value
        square = ws.range(f'C{line}').value
        floor = ws.range(f'D{line}').value
        pred = predict_apt_price(year,square,floor)
        ws.range(f'E{line}').value = pred
    wb.save()
    wb.close()

if __name__ == "__main__" :
    main()
