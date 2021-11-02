from django.forms import ModelForm, Textarea
from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'students'
    ordering = ['-created_at']

