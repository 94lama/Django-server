from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from  rest_framework_simplejwt import exceptions
#from django.utils.decorators import decorator_from_middleware
#from django.middleware.csrf import CsrfViewMiddleware
from rest_framework.request import Request
from jobs.models import Job
import json

def authenticate(token):
    auth = JWTAuthentication()
    token = auth.get_validated_token(token)
    token = auth.get_user(token)
    user = User.objects.get(username=token)
    return user

# Create your views here.
def index(request:Request):
    jobs = []
    for item in Job.objects.all():
        jobs.append(item.__obj__())
    response = HttpResponse(json.dumps(jobs))
    response.headers['Content-Type'] = 'application/json'
    return response

def job_detail(request:Request, id):
    try:
        job = Job.objects.get(id=id).__obj__()
        if request.headers.get('Authorization'):
            jwt_authentication = JWTAuthentication()
            user = jwt_authentication.authenticate(request)
            """ print(auth_user[1])
            user = User.objects.get(id=auth_user.user_id)
            print(user) """
            job['hasPermission'] = True if user and user[0].is_staff else False
            return HttpResponse(json.dumps(job))
        else: return HttpResponse(json.dumps(job))
    except exceptions.InvalidToken: return HttpResponse(json.dumps(job))


#@decorator_from_middleware(CsrfViewMiddleware)
def my_jobs(request:Request):
    body = json.loads(request.body)
    try:
        user = authenticate(body['token'])
    except exceptions.InvalidToken: return HttpResponse(status=401)
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
        job.client = user
        job.title = body['title']
        job.location = body['location']
        job.description = body['description']
        job.save()
        response = HttpResponse('Ok', status=200)
        return response
    elif not user.is_auth: return HttpResponse("Unauthorized", status=401)
    else: return HttpResponse("Error", status=400)

def edit(request:Request):
    body = json.loads(request.body)
    user = authenticate(body['token'])
    if user and user.is_staff:
        job = Job.objects.get(id=body['id'])
        job.title = body['title']
        job.location = body['location']
        job.description = body['description']
        job.save()
        response = HttpResponse('Ok', status=200)
        return response
    elif not user.is_staff: return HttpResponse("Unauthorized", status=401)
    else: return HttpResponse("Error", status=400)