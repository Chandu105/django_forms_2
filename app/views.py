from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}

    if request.method=='POST':
        FDTO=TopicForm(request.POST)
        if FDTO.is_valid():
            tn=FDTO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
            WO.save()
            return HttpResponse('webpage is inserted')
        else:
            return HttpResponse('invalid data')

    
    return render(request,'insert_webpage.html',d)


def insert_access(request):

    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            wn=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(pk=wn)
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            AO.save()
            return HttpResponse('accessrecord is inserted')
        else:
            return HttpResponse('invalid data')
    
    return render(request,'insert_access.html',d)