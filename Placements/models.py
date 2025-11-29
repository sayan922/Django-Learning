from django.db import models
from django.utils import timezone
# Create your models here.

class Companies(models.Model):
    COMPANY_TYPES = [
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('HC', 'Healthcare'),
        ('ED', 'Education'),
        ('MFC', 'Manufacturing')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company_images/')
    drive_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50,choices=COMPANY_TYPES)
    description = models.TextField(default=' ')


def __str__(self): #dunder string
        return self.name