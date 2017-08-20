from django.shortcuts import render
from django.http import httpReponse

def login(request):
    if request.usr.is_authenticated():
        return HttpRespose('login in at port 9000')
    else:
        return HttpResponse('not login at port 9000')


