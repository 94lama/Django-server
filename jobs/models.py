from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default='No title')
    location = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title
    def __obj__(self):
        return {'client': self.client.username, 'title': self.title, 'location': self.location, 'description': self.description}
        