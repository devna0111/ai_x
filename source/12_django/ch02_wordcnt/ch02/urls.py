"""
URL configuration for ch02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
# from wordcnt import views as wordcnt_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index, name="index"), # name을 왜 쓸까?
    path("test/",views.test, name="test"), # <a href = "{% url 'test' %}">TEST_name으로 요청해보기</a> 이렇게 이동이 가능하다
    path("showId/<int:id>/",views.showIntId, name="showIntId"),
    path("showId/<str:id>/",views.showStrId, name="showStrId"),
    # path("showId/문자",),
]
