from django.db import models

# Create your models here.
class Student(models.Model): # student_student(테이블명 : 앱명_클래스명소문자)
    id = models.AutoField(primary_key=True) # 자동으로 생성되는 아이디
    name = models.CharField(max_length=100, unique=True) # 이름
    major = models.CharField(max_length=100, null=True, blank=True) # 전공, null의 default = False, blank=True : required=true 속성 삭제
    age = models.IntegerField(default=0) # 나이
    grade = models.CharField(default=1)
    
    def __str__(self): # 아이디를 출력하는 메서드
        return "{}:{}({}, {}세 {}학년)".format(self.id, self.name, self.major, self.age, self.grade)