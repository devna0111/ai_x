from django.shortcuts import render, get_object_or_404, redirect
from student.models import Student # from .models import Student
from django.contrib import messages # 유용한 기능 모음
# Create your views here.
def list(request):
    students = Student.objects.all()
    return render(request,
                "student/list.html",
                context={"students":students})

def get(request, id) : # int 형태 체크(urls.py에서 전달할 때 int로 )
    # print("★", type(id))
    # student = Student.objects.get(id=id)
    # return render(request,
    #             "student/get.html",
    #             context={"student":student})

    # 해당 id가 없을경우 404에러 반환
    # student = get_object_or_404(Student, id=id) 
    # return render(request,
    #             "student/get.html",
    #             context={"student":student})

    # try_exception으로 처리
    try :
        student = Student.objects.get(id=id)
        return render(request,
                "student/get.html",
                context={"student":student})
    except Student.DoesNotExist:
        # 존재하지 않는 ID로 검색할 경우
        messages.error(request, f"{id}번에 해당하는 학생이 없습니다. 학생 목록으로 돌아갑니다.")
        return redirect("student:list")
    
def delete(request, id:int) -> redirect:
    # try :
    #     student = Student.objects.get(id=id)
    #     student.delete()
    #     messages.success(request, f"{id}번에 해당하는 학생이 삭제되었습니다. 학생 목록으로 돌아갑니다.")
    #     return redirect("student:list")
    # except Student.DoesNotExist:
    #     messages.error(request, f"{id}번에 해당하는 학생이 없습니다. 학생 목록으로 돌아갑니다.")
    #     return redirect("student:list")
    student = Student.objects.filter(id=id) # 없는 경우 []반환
    if student :
        student.delete()
        messages.success(request, f"{id}번에 해당하는 학생이 삭제되었습니다. 학생 목록으로 돌아갑니다.")
        return redirect("student:list")
    else:
        # 존재하지 않는 Id로 검색하는 경우
        messages.error(request, f"{id}번에 해당하는 학생이 없습니다. 학생 목록으로 돌아갑니다.")
        return redirect("student:list")