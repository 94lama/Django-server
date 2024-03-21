from django.shortcuts import HttpResponse
import json

def login(request):
    #if request.method == 'POST':
        username = request.body
        return HttpResponse(request.COOKIES)
    #else: return HttpResponse(status=400)