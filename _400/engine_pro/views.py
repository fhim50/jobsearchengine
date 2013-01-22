# Create your views here.
from engine_pro.start_crawler import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

def start_crawler(request):
    maximum_depth=1
    maximum_pages=1
    crawl_web('http://joblistghana.com',maximum_pages,maximum_depth)
    return HttpResponse('crawler started')
@csrf_exempt
def search(request):
	return render_to_response('prototype/search.html',dict(usr = request.user))
