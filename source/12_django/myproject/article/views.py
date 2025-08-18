from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView, UpdateView,DeleteView
from article.models import Article
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# /article/ : 1 page 
# /article/?page=2 : 2 page
# def article_list(request):
#     articles = Article.objects.all()
#     paginator = Paginator(articles, 3)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)
#     return render(request,
#                 "article/article_list.html",
#                 {"article_list":page_obj,
#                 "page_obj": page_obj},
#                 )

article_list = ListView.as_view(model=Article, 
                                paginate_by=3, # 1 page => 3 data
                                # template_name="article/article_list.html",
                                ) 
article_new = CreateView.as_view(model=Article, fields="__all__")
article_detail = DetailView.as_view(model=Article)
article_edit = UpdateView.as_view(model=Article, fields="__all__")
article_delete = DeleteView.as_view(model=Article, 
                                    success_url=reverse_lazy("article:list"))

# def article_list(request):
# 	pass
# def article_new(request):
# 	pass
# def article_detail(request):
# 	pass
# def article_edit(request):
# 	pass
# def article_delete(request):
# 	pass