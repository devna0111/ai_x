# flask를 사용하기 위한 패키지 설치 : pip install flask
# Flask라는 마이크로 프레임워크(micro Framework)를 사용하기 위해
from flask import Flask
from predict import loaded_model, predict_apt_price

application = Flask(__name__) # 웹 어플리케이션 객체를 생성

@application.route("/hello")

def handler_function() :
    return "<h1>Hello, Flask!</h1>"

# /apt/2005/106/8
@application.route("/apt/<year>/<square>/<floor>")
def aptPredictHandler(year, square, floor) :
    answer = predict_apt_price(year, square, floor)
    return f"<h1>예측금액은 {answer}입니다.</h1>"
    # return {"year":year, "square":square, "floor":floor, "price":answer} # api호출화면같음

if __name__ == "__main__" :
    # params -> debug=True : 서버를 켜놓고 코드를 수정 시 서버 자동 재시작
    application.run(debug=True)