from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse('all_is_done')