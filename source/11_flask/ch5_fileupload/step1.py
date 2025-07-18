# step1
# pip install flask
# jinja2 template include, extends(block)
# file upload(사용자가 업로드한 파일을 서버에 저장) : 업로드 용량 제한

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename # 파일 업로드 처리를 위한 모듈(사용자가 업로드한 파일명에 특수문자를 빼는 모듈)
import os # 업로드 폴더 경로 설정(폴더 없으면 폴더 생성)

UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER) :
    os.makedirs(UPLOAD_FOLDER)

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
# print(app.config)
# 업로드 용량 제한 : 용량 제한 시 403 error
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 10 # 10MB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        # 업로드 파일을 받아 서버 uploads 폴더(var:UPLOAD_FOLDER)에 저장
        file = request.files['file']
        # 파일명에 서버에 영향을 미칠 특수문자 제거를 위해 업로드 파일의 이름을 설정
        save_filename = secure_filename(file.filename)
        file.save(UPLOAD_FOLDER + save_filename)
        return render_template('check.html',upload_filename = file.filename, save_filename = save_filename)

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)