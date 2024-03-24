from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
#from django.middleware.csrf import CsrfViewMiddleware
from rest_framework.request import Request
from django.utils.decorators import decorator_from_middleware
from jobs.models import Job
import json

def authenticate(token):
    auth = JWTAuthentication()
    token = auth.get_validated_token(token)
    token = auth.get_user(token)
    user = User.objects.get(username=token)
    return user

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
    user = authenticate(body.token)
    if user:
        jobs = []
        for item in Job.objects.filter(client=user):
            jobs.append(item.__obj__())
        response = HttpResponse(json.dumps(jobs))
        response.headers['Content-Type'] = 'application/json'
        return response
    else : return HttpResponse(status=400)

def create(request:Request):
    body = json.loads(request.body)
    user = authenticate(body['token'])
    if user:
        job = Job()
        print(job)

        job.client = user
        job.title = body['title']
        job.location = body['location']
        job.description = body['description']
        print(job)
        job.save()
        response = HttpResponse('Job created!', status=200)
        return response
    elif not user.is_auth: return HttpResponse("Unauthorized", status=401)
    else: return HttpResponse("Error", status=400)