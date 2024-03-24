from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
#from django.middleware.csrf import CsrfViewMiddleware
from rest_framework.request import Request
from django.utils.decorators import decorator_from_middleware
from jobs.models import Job
import json

# Create your views here.
def index(request):
    jobs = []
    for item in Job.objects.all():
        jobs.append(item.__obj__())
    response = HttpResponse(json.dumps(jobs))
    response.headers['Content-Type'] = 'application/json'
    return response

#@decorator_from_middleware(CsrfViewMiddleware)
def my_jobs(request:Request):
    body = json.loads(request.body)
    auth = JWTAuthentication()
    token = auth.get_validated_token(body['token'])
    token = auth.get_user(token)
    user = User.objects.get(username=token)
    jobs = []
    for item in Job.objects.filter(client=user):
        jobs.append(item.__obj__())
    response = HttpResponse(json.dumps(jobs))
    response.headers['Content-Type'] = 'application/json'
    return response