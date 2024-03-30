from django.db import models
from django.contrib.auth.models import User

# Add linked classes here

# ///[Job]
class Job(models.Model):
    STATUS = [
        (0, 'Created'),
        (1, 'Assigned'),
        (2, 'Done'),
        (3, 'Approved')
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(choices=STATUS, default=0)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='worker')
    title = models.CharField(max_length=200, default='No title')
    location = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title
    def __obj__(self):
        return {
            'id': self.id,
            'status': self.status,
            'worker': self.worker.username if self.worker else None,
            'client': self.client.username,
            'title': self.title,
            'location': self.location,
            'description': self.description,
        }