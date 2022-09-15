from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

def calender(request):
    return render(request, 'calender.html')