from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.name}"


class fly(models.Model):
    Flight_Name = models.CharField(max_length =100, default="None")
    From = models.CharField(max_length =100, default="None")
    To = models.CharField(max_length=100, default="None")
    Date = models.DateField(default=None)
    Price = models.PositiveIntegerField()
    Duration= models.CharField(max_length=100, default="1 Hour")
    category = models.ForeignKey(category, on_delete = models.PROTECT,null=True)

class Ticket(models.Model):
    TicketNo = models.PositiveIntegerField()
    Name = models.CharField(max_length = 100, default= "None")
    Flight_Name = models.CharField(max_length = 100, default= "None")
    From = models.CharField(max_length = 100, default= "None")
    To = models.CharField(max_length = 100, default= "None")

class Passenger(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length = 100)
    fly_id = models.ForeignKey(fly, on_delete = models.CASCADE)

    




    
    

    
