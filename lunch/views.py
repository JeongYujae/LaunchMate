from datetime import datetime
from datetime import timedelta
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from lunch.models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


def index(request):
    return render(request, 'main.html')

def calender(request):
    return render(request, 'calender.html')


def select(request):
    # 오늘 내일 날짜 로딩하는 방법
    today=(datetime.today().date())
    today_view=today.strftime("%Y.%m.%d")
    tomorrow = today + timedelta(days=1)
    tomorrow_view=tomorrow.strftime("%Y.%m.%d")
    context={'today':today_view, 'tomorrow':tomorrow_view}
    

    return render(request, 'select.html',context=context)


# 투표해서 참석
def lunch_join(reqeust,pk):
    pass
    #TODO

# 투표에서 캔슬
def lunch_cancel(reqeust,pk):
    pass
    #TODO

# 메뉴 


@login_required
def new_appointment(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            messages.success(request, '약속이 등록되었습니다!')
            return redirect(post)
    else:
        form=AppointmentForm()

    return render(request,"lunch/select.html",{
        "form":form,
    })


def join_appointment(request,pk):
    appointment=get_object_or_404(Appointment, pk=pk)
    appointment.participate_user_set.add(request.user)
    messages.success(request,"약속에 참여했습니다.")
    redirect_url=request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)


def revoke_appointment(request,pk):
    appointment=get_object_or_404(Appointment, pk=pk)
    appointment.participate_user_set.remove(request.user)
    messages.success(request,f"약속 참여에 취소했습니다.")
    redirect_url=request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)





