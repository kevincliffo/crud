from django.db import models
from datetime import datetime

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    date_added = models.DateField(default=datetime.now)
    slug = models.CharField(max_length=500)
    finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name