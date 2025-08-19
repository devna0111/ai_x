import os.path
from django.db import models
import time
from datetime import datetime
from django.urls import reverse
from myproject import settings
from django.shortcuts import get_object_or_404
STATUS_CHOICES = (
  ('d', 'Draft'),
  ('p', 'Published'),
  ('w', 'Withdrawn'),
)
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    body = models.TextField(verbose_name="본문")
    status = models.CharField(max_length=1, 
                              choices=STATUS_CHOICES,)
    photo = models.ImageField(blank=True, # DB에는 파일명만 저장, _media 폴더에 저장
                              upload_to="article/%Y/%m/%d",# _media/article/2025/08/19 폴더에 저장
                              verbose_name="첨부파일"
                              ) 
    # DB에는 _media/article/2025/08/19/a.png 저장, 첨부파일은 upload_to에 저장
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article:detail", args=[self.id]) # create나 update 후 url 연결
    
    def delete(self, *args, **kwargs): # 상위 클래스에서 어떤 파라미터를 썼나 체크할 때는 kw를 기입하면 자동완성으로 확인됨
        # DB 삭제전 self.photo 파일 삭제
        if self.photo: # 파일 첨부가 있는 지 체크
          # file_path = os.path.join(settings.BASE_DIR, "_media" ,str(self.photo))
          file_path = os.path.join(settings.MEDIA_ROOT, str(self.photo))
          print(file_path, "파일을 삭제하고 DB에서 delete")
          if os.path.exists(file_path):
            os.remove(file_path)
        super().delete(args, kwargs)
        # super().delete(args, kwargs) # 기존 delete : DB에서 현재 instance delete
    
    def save(self, *args, **kwargs) :
      if self.pk : # 수정 할 때
        old_instance = get_object_or_404(Article, pk = self.pk)
        if old_instance.photo and old_instance.photo != self.photo : # 기존 첨부파일을 수정한 경우
          file_path = os.path.join(settings.MEDIA_ROOT, str(old_instance.photo))
          if os.path.exists(file_path):
            os.remove(file_path)
      super().save(args, kwargs)
    
    class Meta :
        ordering = ["-id"]
    