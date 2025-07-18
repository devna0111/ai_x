# pip install flask_wtf : flask에서 form 관리 기능
    # CSRF 보호 정책 설정
    # 쉽고 유연한 폼 적용하여 유효성 검증, input 태그 생성

from flask import Flask, render_template # request를 통해 데이터를 html에서 받는 게 아니라 flask에서 관리하는 form으로 받는..
from flask_wtf import FlaskForm # form 관리 기능
from flask_wtf.file import FileField, FileRequired # 파일 업로드 기능
from werkzeug.utils import secure_filename # 파일 업로드 처리를 위한 모듈(사용자가 업로드한 파일명에 특수문자를 빼는 모듈)
from fileinfo import info # 파일 정보 가져오기
import os

UPLOAD_FOLDER = 'uploads/' # 업로드 폴더 설정
if not os.path.exists(UPLOAD_FOLDER) : # 업로드 폴더 생성
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
print(app.config) # 모든 dict_keys()는 대문자로 체크되어야 함
app.config['max_content_length'] = 1024 * 1024 * 5 # 5MB
app.config['SECRET_KEY'] = 'secret!'

class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired()]) # 업로드한 파일 객체
filelist = os.listdir(UPLOAD_FOLDER)
@app.route('/', methods=['GET', 'POST']) # 폴더 안에 파일들의 정보를 listup
def index():
    form = FileForm() # form 객체 생성
    if form.validate_on_submit() : # form 데이터가 유효한 지(POST요청이 유효하게 들어왔는 지) 체크
        file = form.files.data # 업로드한 파일 객체
        safe_filename = secure_filename(file.filename) # 사용자가 업로드한 파일명에 특수문자를 빼는 모듈
        file.save(UPLOAD_FOLDER + safe_filename) # 업로드 파일을 받아 서버 uploads 폴더(var:UPLOAD_FOLDER)에 저장
        ctime, mtime, atime, size = info(safe_filename) # 파일 정보 가져오기
        return render_template('check.html',
                                fileinfo={'ctime':ctime, 'size':size}, # check.html에 파일 정보를 넣어줌
                                filelist=filelist) 
    else : # 유효하지 않은 폼 데이터 : GET 방식이거나 POST요청이 유효하지 않던지
        return render_template('upload.html', form=form, filelist=filelist) # upload.html에 form 객체를 넣어줌
    
if __name__ == '__main__':
    app.run(debug=True, port=80)    