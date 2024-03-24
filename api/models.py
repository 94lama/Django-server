from rest_framework.views import APIView
from rest_framework.response import Response
import json

# Create your models here.
class TestView(APIView):
    def get(self, request):
        return Response(json.dumps(request.headers), status=200)