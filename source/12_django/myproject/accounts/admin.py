from django.contrib import admin
from accounts.models import Profile

# Register your models here.
admin.site.register(Profile) # admin 페이지에서 Profile 테이블 액세스 가능하도록