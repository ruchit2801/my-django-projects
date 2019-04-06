from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {'insert_content':'Hello! I am from first app'}
    return render(request,'first_app/index.html',context=date_dict)
# Create your views here.
