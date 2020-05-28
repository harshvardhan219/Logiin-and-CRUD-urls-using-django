from django.db import models

# Create your models here.
class Stream(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    stu_code = models.CharField(max_length=200)  
    mobile = models.CharField(max_length=200) 
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)