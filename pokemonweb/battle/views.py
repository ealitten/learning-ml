from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'battle/index.html', {})

def pokemon(request):
    return HttpResponse('Pokemon page')
    