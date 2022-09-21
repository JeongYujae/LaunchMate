from datetime import datetime
from datetime import timedelta
from django.shortcuts import render

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