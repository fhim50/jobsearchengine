# Create your views here.
from engine_pro.start_crawler import *
from django.http import HttpResponseRedirect, HttpResponse

def start_crawler(request):
    maximum_depth=2
    maximum_pages=3
    crawl_web('http://www.joblistghana.com',maximum_pages,maximum_depth)
    return HttpResponse('crawler down')
