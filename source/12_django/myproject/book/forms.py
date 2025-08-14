from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from .models import Book

# def min_length_3_validator(value): # 이런 내용의 validators는 django 내장된 것들이 많음
#     if len(value) < 3:
#         raise forms.ValidationError("최소 3자 이상 입력해주세요.") # 원래 있던 페이지로 에러메세지와 함께 redirect

# class BookForm(forms.Form): # form 객체 생성
#     # pk : 자동 설정
#     title = forms.CharField(label="책제목",
#                             )
#     author = forms.CharField(label="책쓴이",
#                             # null=True,
#                             # blank=True, # null, blank True 설정이면 0글자도 가능
#                             validators=[
#                                 min_length_3_validator,
#                                 # MinLengthValidator(3), # 영문형태로 에러메세지 반환
#                                 ],
#                             )
#     publisher = forms.CharField(label="출판사", required=False,)
#     sales = forms.IntegerField(label="판매가",
#                                 initial=1000,
#                                 validators=[MinValueValidator(0),# 0 이상 입력하지 않으면 에러메세지
#                                             MaxValueValidator(1000000)], # 1000000 이하 입력하지 않으면 에러메세지
#                                 )
#     def save(self, commit=True):
#         book = Book(**self.cleaned_data) # cleaned_data 입력 데이터-> 검증 완료 데이터
#         if commit:
#             book.save() # 저장
#         return book
    
class BookModelForm(forms.ModelForm): # modelform 객체 생성
    class Meta:
        model = Book
        fields = ["title", "author", "publisher", "sales"]
        # fields = "__all__" # 전체 필드 선택