from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.


def create_insert(request):
    
    if request.method=='POST':
        tn=request.POST['tn']
        
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        
        To.save()
        
        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        
        return render(request,'display_topic.html',d)

        
    return render(request,'create_insert.html')


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}

    if request.method=='POST':
        
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        
        TO=Topic.objects.get(topic_name=tn)
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()

        QLWO=Webpage.objects.all()
        d1={'webpage':QLWO}

        return render(request,'display_webpage.html',d1)
        
        return HttpResponse('webpage is created succefully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):  
    if request.method=='POST':
        na=request.POST['na']
        dt=request.POST['dt']
        au=request.POST['au']
        
        AO=AccessRecord.objects.get_or_create(name=na,date=dt,author=au)[0]
        AO.save()

        AO=AccessRecord.objects.all()
        d={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d)

        return HttpResponse('accessrecord is created successfully')

            


    return render(request,'insert_accessrecord.html')    
        

































   
       



