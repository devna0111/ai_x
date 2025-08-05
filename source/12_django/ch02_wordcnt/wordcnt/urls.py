# wordcnt 패키지 urls.py
# /wordcnt : text를 입력하는 form (POST/GET)
# /wordcnt/about : 도움말 페이지
# /wordcnt/result : 입력된 text의 글자수, 단어수, 각 단어 갯수 출력

from django.contrib import admin
from django.urls import path
from wordcnt import views
# from wordcnt import views as wordcnt_views
app_name = "wordcnt" # 요청경로 wordcnt:wordinput 이런식으로 변경
urlpatterns = [
    path("", views.wordinput, name="wordinput"),
    path("about/", views.about, name="about"),
    path("result/", views.result, name="result"),
]