from django.shortcuts import HttpResponse
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Job
import json

query_list = ['id', 'client', 'title', 'location']


# Test environment
class TestView(APIView):
    def get(self, request):
        return Response('Request accepted', status=200)


# Create your views here.
def index(request):
    if request:
        return HttpResponse(json.dumps(request.COOKIES['csrftoken']), status=200)
    jobs = []
    for item in Job.objects.all():
        jobs.append(item.__obj__())
    response = HttpResponse(json.dumps(jobs))
    response.headers['Content-Type'] = 'application/json'
    return response

def job(request: HttpRequest, job_id: int):
    job = Job.objects.get(id=job_id)
    response = HttpResponse(json.dumps(job.__obj__()))
    response.headers['Content-Type'] = 'application/json'
    return response

def search_job(request: HttpRequest, key: str, value: str):
    jobs = []
    if key == 'client':
        for item in Job.objects.all():
            if item.client.username == value:
                jobs.append(item.__obj__())
        response = HttpResponse(json.dumps(jobs))
        response.headers['Content-Type'] = 'application/json'
        return response
    elif key in query_list:
        for item in Job.objects.filter(**{key: value}):
            jobs.append(item.__obj__())
        response = HttpResponse(json.dumps(jobs))
        response.headers['Content-Type'] = 'application/json'
        return response
    else: return HttpResponse(status=400)