from django.contrib import admin
from student.models import Student

# Register your models here.
admin.site.register(Student) # 관리자 화면에 Student 클래스와 연결된 테이블을 등록