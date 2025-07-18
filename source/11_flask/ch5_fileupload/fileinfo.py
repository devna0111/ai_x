# fileinfo.py
# 특정 폴더(UPLOAD_FOLDER = 'uploads/') 안에 파일들의 정보를 listup
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename # 파일 업로드 처리를 위한 모듈(사용자가 업로드한 파일명에 특수문자를 빼는 모듈)
import os
import datetime

UPLOAD_FOLDER = 'uploads/'
# filelist = os.listdir(UPLOAD_FOLDER) # 폴더 안에 파일들의 정보를 listup
# # print(filelist)
# for filename in filelist:
#     ctime = datetime.datetime.fromtimestamp(os.path.getctime(UPLOAD_FOLDER + filename)).strftime('%Y-%m-%d %H:%M:%S') # 파일 생성 시간
#     mtime = datetime.datetime.fromtimestamp(os.path.getmtime(UPLOAD_FOLDER + filename)).strftime('%Y-%m-%d %H:%M:%S') # 파일 수정 시간
#     atime = datetime.datetime.fromtimestamp(os.path.getatime(UPLOAD_FOLDER + filename)).strftime('%Y-%m-%d %H:%M:%S') # 파일 접근 시간
#     size = os.path.getsize(UPLOAD_FOLDER + filename) # 파일 크기
#     print(filename, ctime, mtime, atime, size)

# 코드 간소화를 위해 함수화
def stamp2datetime(stamp):
    '''parameter : timestamp => return : datetime'''
    return datetime.datetime.fromtimestamp(stamp)

def info(filename):
    '''parameter : filename => return : ctime, mtime, atime, size'''
    ctime=stamp2datetime(os.path.getctime(UPLOAD_FOLDER + filename)) # 유닉스 시간
    mtime=stamp2datetime(os.path.getmtime(UPLOAD_FOLDER + filename)) # 유닉스 시간
    atime=stamp2datetime(os.path.getatime(UPLOAD_FOLDER + filename)) # 유닉스 시간
    size=os.path.getsize(UPLOAD_FOLDER + filename) # 바이트 
    if size >= 1024 * 1024 : # MB
        size = size / (1024 * 1024)
        size = f'{size:.2f}MB'
    elif size >= 1024 : # KB
        size = size / 1024
        size = f'{size:.2f}KB'
    else : # B
        size = f'{size:.2f}B'
    return ctime, mtime, atime, size

if __name__ == "__main__" :
    filelist = os.listdir(UPLOAD_FOLDER)
    for filename in filelist:
        ctime, mtime, atime, size = info(filename)
        print(filename, ctime, mtime, atime, size)
