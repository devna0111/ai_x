from django.urls import path, register_converter
from student import views # from . import views
from .converters import IdConverter

# "" -> student list 출력
# "/student" -> student list 출력
# "/student/get/1" -> student id가 1번인 학생의 데이터 상세보기 (student:get)
# "/student/del/1" -> student id가 1번인 학생 데이터 삭제 (student:del)

app_name = "student"
register_converter(IdConverter, "Id")
urlpatterns = [
    path("", views.list, name="list"),
    path("get/<Id:id>", views.get, name="get"),
    path("del/<Id:id>", views.delete, name='del')
    ]