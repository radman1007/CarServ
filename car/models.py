from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    service = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    accept = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name
   
    
class Comment(models.Model):
    post = models.ForeignKey(Service,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class News(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to="Team")
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name