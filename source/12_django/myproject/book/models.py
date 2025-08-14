from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.urls import reverse

def min_length_3_validator(value): # 이런 내용의 validators는 django 내장된 것들이 많음
    if len(value) < 3:
        raise forms.ValidationError("최소 3자 이상 입력해주세요.") # 원래 있던 페이지로 에러메세지와 함께 redirect

# Create your models here.
class Book(models.Model): # book_book 테이블 생성
    # pk : 자동 설정
    title = models.CharField(verbose_name="책제목",
                            max_length=50,
                            )
    author = models.CharField(verbose_name="책쓴이",
                            max_length=50,
                            # null=True,
                            # blank=True, # null, blank True 설정이면 0글자도 가능
                            validators=[
                                min_length_3_validator,
                                # MinLengthValidator(3), # 영문형태로 에러메세지 반환
                                ],
                            )
    publisher = models.CharField(verbose_name="출판사",
                            max_length=50,
                            blank=True,
                            null=True,
                            )
    sales = models.IntegerField(verbose_name="판매가",
                                default=1000,
                                validators=[MinValueValidator(0),# 0 이상 입력하지 않으면 에러메세지
                                            MaxValueValidator(1000000)], # 1000000 이하 입력하지 않으면 에러메세지
                                )
    ip = models.GenericIPAddressField(blank=True, null=True) # 주소 입력
    publication_date = models.DateField(verbose_name="출판일",
                                        auto_now_add=True, # 자동 생성 시간
                                        blank=True,
                                        null=True,
                                        )
    def __str__(self) :
        return "{}({}) {}원 from {}".format(self.title, self.author, self.sales, self.ip)
    
    def get_absolute_url(self):
        return reverse("book:list")
    
    class Meta :
        ordering = ["-publication_date"]
        unique_together = (("title", "author"),) # title과 author 가 "동시에" 같으면 저장 불가