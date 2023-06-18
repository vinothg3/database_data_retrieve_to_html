from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    #lot=Topic.objects.all()
    lot=Topic.objects.filter(Table_name='cricket')
    print(lot)
    d={'topic':lot}
    return render(request,'display_topic.html',d)
def display_webpage(request):
    #low=Webpage.objects.all()
    low=Webpage.objects.filter(Table_name='cricket')
    d={'web':low}
    return render(request,'display_webpage.html',d)

def display_access(request):
    loa=Access.objects.all()
    d={'access':loa}
    return render(request,'display_access.html',d)
