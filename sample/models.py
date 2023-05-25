from time import time
from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.TextField(max_length=20, null=False, blank=False)
    date_of_birth = models.DateField()
    location = models.TextField(max_length=10)

    def __str__(self):
        return self.name

class Consult(Patient):
    problem = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now=True)