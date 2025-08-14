from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .forms import BookForm
from .forms import BookModelForm
from .models import Book
# 1. form없이 걍 2. form객체생성후(6장) 3. DjangoGenericView 이용 4. GenericView 상속(7장)

book_list = ListView.as_view(model=Book) # generic view 활용
# 위 코드는 아래와 동일(변수명 같아야함)
# def book_list(request):
#     return render(request,
#                 "book/book_list.html",
#                 {"book_list": Book.objects.all()},
#                 )

def book_new(request): # GET : template / POST : 매개변수를 받아서 db에 저장(save()) -> book:list
    if request.method == "POST" :
        print(request.POST)
        # title = request.POST.get("title")
        # author = request.POST["author"]
        # publisher = request.POST["publisher"]
        # sales = int(request.POST["sales"])
        # ip = request.META["REMOTE_ADDR"] # 요청한 client의 ip 주소
        # book = Book(title=title,author=author, publisher=publisher, sales=sales,ip=ip,)
        # book.save()
        # return redirect(book) # model을 생성할 떄 get_absolute_url 함수를 사용하여 이 값으로 return
        form = BookModelForm(request.POST) # request.POST를 받는 form 생성
        # print("★",form.is_valid()) # 유효성검사 결과
        # print("유효성 검사 결과 :", form.cleaned_data)
        if form.is_valid(): # 유효성 검사 결과가 True 면
            book = Book(**form.cleaned_data) # 유효성 검사 완료 데이터 저장
            book.ip = request.META["REMOTE_ADDR"] # 요청한 client의 ip 주소
            book.save() # 저장
            return redirect(book) # model을 생성할 떄 get_absolute_url 함수를 사용하여 이 값으로 return
        else:
            print("유효성 검사 결과 :", form.errors)
            return render(request,
                        "book/book_form.html",
                        {"form": form}, # form 생성
                        )
    elif request.method == "GET" :
        form = BookModelForm() # modelform 생성
        return render(request,
                    "book/book_form.html",
                    {"form": form},
                    )