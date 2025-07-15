# app.py
from flask import Flask, render_template, request, abort
from models import Member
from filters import mask_password

app = Flask(__name__)
app.template_filter("mask_pw")(mask_password) # 필터 추가

@app.errorhandler(404) # 예외 페이지 처리
def errorhandler(error):
    return render_template("404_pageNotFound.html"), 404    

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("2_postetc/index.html")

@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "GET":
        return render_template("2_postetc/join.html")
    elif request.method == "POST": # POST방식으로 파라미터 데이터 받기
        # name = request.form.get("name") # POST 방식에서 데이터 받는 방법
        # id = request.form.get("id") # id 파라미터를 type= "number"로 보내옴
        # # print(type(id)) # <class 'str'>
        # pw = request.form.get("pw")
        # addr = request.form.get("addr")
        # request.form.to_dict() => {'name':name, 'id':id, 'pw':pw, 'addr':addr}
        new_member = Member(**request.form.to_dict())
        print(type(new_member.id))
        return render_template("2_postetc/result.html", member = new_member)

@app.route("/update/<name>/<id>/<pw>/<addr>", methods=["PATCH"])
def update(name, id, pw, addr) :
    print("update 왔다")
    return f"{name}님 정보가 수정되었습니다."

if __name__ == "__main__":
    app.run(debug=True)