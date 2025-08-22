'''
django.contrib.messages.context_processors 원리를 알기 위해 구현
'''
from datetime import datetime

def myproject(request) :
    return {
        # "user" : request.user, 기본 설정값이어서 모든 페이지에 내용이 우선 전달됨
        "now" : datetime.now().strftime("%y-%m-%d (%p) %I:%M:%Ss"),
            }