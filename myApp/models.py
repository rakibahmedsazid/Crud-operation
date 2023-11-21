from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    address=models.TextField()
    email=models.EmailField()
    img=models.ImageField(upload_to="pics",null=True,blank=True)
    
    
    

    
    

