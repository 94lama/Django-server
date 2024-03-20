from django.shortcuts import HttpResponse
from jobs.models import Job

# Create your views here.
def index(request):
    jobs = []
    for item in Job.objects.all():
        jobs.append(item.__obj__())
    response = HttpResponse(jobs)
    return response