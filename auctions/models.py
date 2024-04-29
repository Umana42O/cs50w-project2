from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auctions(models.Model):
    categories = [
    ("Electrodomésticos", "Electrodomésticos"),
    ("Tecnología", "Tecnología"),
    ("Ropa", "Ropa"),
    ("Coleccionables", "Coleccionables"),
    ("Juguetes", "Juguetes"),
    ("Otros", "Otros"),
]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    initialPrice = models.FloatField()
    is_active = models.BooleanField(default= True)
    category = models.CharField(max_length=20,default="Otros", choices=categories)

    def __str__(self):
        return f"{self.name} {self.initialPrice} {self.is_active} {self.category}"

class comments(models.Model):
    auction = models.ForeignKey(auctions, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_auction} {self.comment} {self.id_user}"
    
class offers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.FloatField()
    auction = models.ForeignKey(auctions, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.id_user} {self.offer} {self.id_auction} {self.date}"
    
class user_auctions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(auctions, on_delete=models.CASCADE)

