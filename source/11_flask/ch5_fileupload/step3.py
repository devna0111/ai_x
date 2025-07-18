# 파일 첨부 화면 + 첨부했던 파일 목록(다운로드+삭제)
from flask import Flask, render_template # request를 통해 데이터를 html에서 받는 게 아니라 flask에서 관리하는 form으로 받는..
from flask_wtf import FlaskForm # form 관리 기능
from flask_wtf.file import FileField, FileRequired # 파일 업로드 기능
from werkzeug.utils import secure_filename # 파일 업로드 처리를 위한 모듈(사용자가 업로드한 파일명에 특수문자를 빼는 모듈)
from fileinfo import info # 파일 정보 가져오기
import os
from flask import send_file # 파일 다운로드 시 필요
from flask import redirect, url_for # 파일 삭제 후 '/' 요청 경로로 redirect
import datetime
UPLOAD_FOLDER = 'uploads/' # 업로드 폴더 설정

app = Flask(__name__)
print(app.config) # 모든 dict_keys()는 대문자로 체크되어야 함
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 5 # 5MB
app.config['SECRET_KEY'] = 'secret!'

class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired()]) # 업로드한 파일 객체

@app.route('/', methods=['GET', 'POST']) # 폴더 안에 파일들의 정보를 listup
def index():
    form = FileForm() # form 객체 생성
    if form.validate_on_submit() : # form 데이터가 유효한 지(POST요청이 유효하게 들어왔는 지) 체크
        file = form.files.data # 업로드한 파일 객체
        safe_filename = secure_filename(file.filename) # 사용자가 업로드한 파일명에 특수문자를 빼는 모듈
        # 파일 중복 체크 하면 좋다
        if safe_filename in os.listdir(UPLOAD_FOLDER) : # 업로드 파일이 이미 존재하는지 체크
            safe_filename = safe_filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") # 중복 체크 후 이름을 변경
        file.save(UPLOAD_FOLDER + safe_filename) # 업로드 파일을 받아 서버 uploads 폴더(var:UPLOAD_FOLDER)에 저장
        ctime, mtime, atime, size = info(safe_filename) # 파일 정보 가져오기
        return render_template('check.html',
                                fileinfo={'ctime':ctime, 'size':size}, # check.html에 파일 정보를 넣어줌
                                ) 
    else : # 유효하지 않은 폼 데이터 : GET 방식이거나 POST요청이 유효하지 않던지
        # 업로드 폴더의 파일 정보를 listup
        filelist = os.listdir(UPLOAD_FOLDER)
        infos = [] # 파일 정보 목록을 담을 리스트(파일명, 생성시간, 수정시간, 크기)
        for filename in filelist:
            ctime, mtime, atime, size = info(filename)
            fileinfo = {'name':filename, 'ctime':ctime, 'mtime':mtime, 'size':size}
            infos.append(fileinfo)
        return render_template('home.html', form=form, infos=infos) # upload.html에 form 객체를 넣어줌

@app.route('/delete/<filename>')
def delete(filename) :
    os.remove(UPLOAD_FOLDER + filename)
    # return redirect(url_for("index"))
    return redirect("/")

@app.route('/download/<filename>')
def download(filename) :
    return send_file(UPLOAD_FOLDER +filename,
                    as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=80)    