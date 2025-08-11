from django.contrib import admin
from blog.models import Post
# Register your models here.

admin.site.register(Post) # admin 페이지에서 POST 테이블 액세스 가능하도록