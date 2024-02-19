from django.db import models

# Create your models here.
class user(models.Model):
    class Meta:
        db_table="user"
        
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)
    Date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class address(models.Model):
    address=models.CharField(max_length=100)
    
class Person(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    address1=models.ForeignKey(address,on_delete=models.CASCADE,related_name="useraddress")
    
    
    
class Employee(models.Model):
    Side_male='M'
    Side_female='F'
    Side_others='O'
    
    choices=[
        (Side_male,'Male'),
        (Side_female,'Female'),
        (Side_others,'Others'),
        
    ]
    name=models.CharField(max_length=100)
    gender=models.CharField(choices=choices,max_length=100)
    
    
    
class Customer(models.Model):
    name=models.CharField(max_length=100)
    users=models.OneToOneField(user,max_length=100,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    
    