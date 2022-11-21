from django.db import models


class Request(models.Model):

    name = models.CharField(max_length=20, default="name")
    surname = models.CharField(max_length=20, default="surname")
    email = models.EmailField(default="email")
    company = models.CharField(max_length=30, default="company")
    message = models.TextField(max_length=200, default="message")
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.surname}, {self.email}, {self.email}, {self.date}"
    
   
class Review(models.Model):

    name = models.CharField(max_length=20,default='')
    message = models.TextField(max_length=200,default='')
    email = models.EmailField(default='')
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.date}"


   
