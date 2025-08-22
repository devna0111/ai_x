from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # 예외 메세지 담는 역할
from django.http import JsonResponse, HttpResponse
from .models import Post
# Create your views here.
def index(request) :
    return JsonResponse({"singer" : "BTS", "song" : ['DNA','FAKE LOVE', "피땀눈물"]},
                        json_dumps_params={'ensure_ascii': False},
                        )

def list(request): # blog:index와 동일
    print("request.user :", request.user) # 로그인 전이면 AnonymousUser, 로그인 후이면 User
    post_list = Post.objects.all()
    return render(request, "blog/index.html", {"post_list": post_list,
                                                # 'user': request.user, # 필요하지 않음
                                                })

def detail(request, post_id):
    # post = Post.objects.get(pk=post_id)
    # post = get_object_or_404(Post, pk=post_id) # 404 상태 처리
    # return render(request, "blog/detail.html", {"post": post})
    post = Post.objects.filter(pk=post_id) # list
    if post :
        return render(request, "blog/detail.html", {"post": post[0]})
    else :
        messages.error(request, "존재하지 않는 게시글 번호입니다.")
        return redirect("blog:index")