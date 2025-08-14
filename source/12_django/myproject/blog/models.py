from django.db import models
import re
from django.forms import ValidationError
# Create your models here.

REGION_CHOICE = (
    ("Europe","유럽"),
    ("Asia", "아시아"),
    ("Oceania","오세아니아"),
    ("America","아메리카"),
)
def lnglat_validator(value):
    if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)', value):
        raise ValidationError('Invalid LngLat. ex:38, 128')

class Tag(models.Model) : # blog_tag 테이블 생성
    # id = models.AutoField(primary_key=True) # PK가 없을 경우 자동 생성
    name = models.CharField(max_length=100,
                            verbose_name="태그명",
                            unique=True,
                            )
    def __str__(self) :
        return self.name
    

class Post(models.Model): # blog_post(앱이름_클래스이름) 테이블 생성
    # id = models.AutoField(primary_key=True) # PK가 없을 경우 자동 생성
    title = models.CharField(verbose_name="제목", # 라벨
                            max_length=100, # VARCHAR2 최대 길이
                            )
    content = models.TextField("내용", # 최대길이 제한 없음 CLOB, TEXT, verbose_name을 기입하지 않아도 첫 파라미터는 라벨
                            )
    created_at = models.DateTimeField(auto_now_add=True) # 자동 생성 시간
    updated_at = models.DateTimeField(auto_now=True) # 자동 수정 시간
    region = models.CharField(max_length=20,
                            choices=REGION_CHOICE,
                            verbose_name="지역",
                            default="Asia") # 예시 선택된 값
    lnglat = models.CharField(max_length=100,
                            verbose_name="경,위도",
                            blank=True,
                            null=True,
                            help_text="경도, 위도 포맷", # 38.5, 125.8 이런 형식으로 입력 => 38, 125
                            validators=[lnglat_validator], # 위도, 경도 입력 검사
                            )
    url = models.URLField(verbose_name="URL", blank=True, null=True) # URL 필드
    tags = models.ManyToManyField(Tag, blank=True, null=True) # 태그 필드
    def __str__(self) : 
        return "제목 : {} - {} 작성 {} 최종수정".format(self.title,
                                                self.created_at,
                                                self.updated_at)
    
    class Meta: # model 속 Meta는 아래 처럼 옵션을 명시할 수 있음
        ordering = ["-updated_at"] # 정렬 옵션

class Comment(models.Model): # blog_comment 테이블 생성
    # id = models.AutoField(primary_key=True) # PK가 없을 경우 자동 생성
    post = models.ForeignKey(Post,
                            on_delete=models.CASCADE, # post 내용을 delete 할 경우 자동 삭제
                            )
    author = models.CharField(
        max_length=20,
        verbose_name="작성자",
        null = True,
        blank = True,
    )
    message = models.TextField(verbose_name="댓글", # 최대길이 제한 없음 CLOB, TEXT, verbose_name을 기입하지 않아도 첫 파라미터는 라벨
                            )
    created_at = models.DateTimeField(auto_now_add=True) # 자동 생성 시간
    updated_at = models.DateTimeField(auto_now=True) # 자동 수정 시간
    def __str__(self) : 
        return "{}글의 댓글 - {}(by {})".format(self.post.id,
                                                self.author,
                                                self.created_at,
                                                self.updated_at)
    class Meta :
        ordering = ["-created_at","-updated_at"] # 정렬 옵션

