from django.db import models
from django.urls import reverse
class Register(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50,blank=False)
    def __str__(self):
        return self.username
class Dept(models.Model):
    dept = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.dept)
class Course(models.Model):
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.course)
