from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def insert_Topic(request):
    TMF=TopicModelForm()
    if request.method=='POST':
        TPF=TopicModelForm(request.POST)
        if TPF.is_valid():
            TPF.save()
            return HttpResponse('Topic insertion data is done')
    return render(request,'insertion_topic.html',{'TMF':TMF})

def insert_Webpage(request):
    WPMF=WebpageModelForm()
    if request.method=='POST':
        WPFD=WebpageModelForm(request.POST)
        if WPFD.is_valid():
            WPFD.save()
            return HttpResponse('Webpage insertion data is done')
    return render(request,'insertion_Webpage.html',{'WPMF':WPMF})

def insert_AccessRecord(request):
    ARMF=AcceeseRecordModelForm()
    if request.method=='POST':
        ARFO=AcceeseRecordModelForm(request.POST)
        if ARFO.is_valid():
            ARFO.save()
            return HttpResponse('AccessRecord insertion data is done')
    return render(request,'insertion_accessrecord.html',{'ARMF':ARMF})