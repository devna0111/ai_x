# python -m venv .venv # 가상환경 생성 방법 1
# ctrl + shift + p => select interpretter => 가상환경 만들기 => venv로 가상환경 만들기 => 인터프리터 경로 입력 => 찾기
# => python.exe 파일 찾기 (아나콘다 사용 했으면 아나콘다 폴더로 가서 찾을 수 있음) # 가상환경 생성 방법2
# 가상환경 활성화 : .venv\Scripts\activate
# python -m pip install --upgrade pip # 1방법 선택하거나 가끔 관련 경고메세지 발생하면 실행하기
# 필요한 라이브러리 pip install
from flask import Flask, render_template # 앱객체 만들기, html 랜더링
from flask import  request, abort # get방식으로 파라미터 데이터 받기 request, 강제 예외 처리를 위한 abort
from models import Member
from filters import mask_password

app = Flask(__name__)

# # 필터링 추가 (str -> str문자개수 만큼 *처리) pw
app.template_filter("mask_pw")(mask_password)
# @app.template_filter("mask_pw") # 이건 필터라고 명시하는 방법
# def mask_password(password) :
#     return "*" * len(password)

@app.route("/user/<name>", methods=["GET"]) # /user/hong
def viewFunction_handlerFunction(name) :
    return f"<h1>{name}님, 안녕하세요!</h1>"

@app.route("/user", methods = ['GET']) # /user?name=hong&....
def test() :
    name = request.args.get('name') # requset.args => dict() 타입, get방식으로 파라미터 데이터 받기
    if name :
        return f"<h1>{name}님, 테스트페이지입니다!</h1>"
    else :
        abort(404)

@app.errorhandler(404) # 404 예외 페이지 처리
def errorhandler(error) :
    return render_template("404_pageNotFound.html"), 404

@app.route("/", methods = ["GET","POST"]) 
def index() :
    return render_template("index.html")

@app.route("/join_form", methods = ["GET"])
def join_form() :
    return render_template("1_onlyget/join_form.html")

@app.route("/join", methods=["GET"])
def join() :
    name = request.args.get('name')
    id = request.args.get('id')
    pw = request.args.get('pw')
    addr = request.args.get('addr')
    new_member = Member(name,id,pw,addr)
    return render_template("result.html", member = new_member)

if __name__ == "__main__" :
    app.run(debug=True)
