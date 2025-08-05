from django.shortcuts import render, HttpResponse

# Create your views here.
def wordinput(request):
    return render(request,
                "wordcnt/wordinput.html")

def about(request):
    return render(request,
                "wordcnt/about.html")

def result(request):
    """fulltxt 파라미터 값을 입력 받아 글자수, 단어수, 출현단어 등을 templates(result.html)에 출력하는 함수"""
    # fulltxt = request.POST.get("fulltxt", "")
    fulltxt = request.GET.get("fulltxt", "")
    strlength = len(fulltxt)
    words = fulltxt.split()
    wordcnt = len(words)
    words_dic = dict()
    for word in words:
        if word in words_dic.keys():
            words_dic[word] += 1
        else:
            words_dic[word] = 1
    context = {"fulltxt" : fulltxt,
                "strlength" : strlength,
                "wordcnt" : wordcnt,
                "word_dic" : words_dic.items()}
    return render(request,
                "wordcnt/result.html",
                context)