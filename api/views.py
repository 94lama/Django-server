from django.shortcuts import HttpResponse
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