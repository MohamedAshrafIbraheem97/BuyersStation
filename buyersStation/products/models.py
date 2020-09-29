from django.db import models
from users.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    old_price = models.FloatField()
    new_price = models.FloatField(blank= True)
    creation_date = models.DateTimeField(auto_now_add= True)
    quantity = models.IntegerField()
    seller = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.product_name, self.description


class review(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE) 
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    comment = models.TextField(blank= True)
    rate = models.IntegerField()

    def __str__(self):
        return self.product, self.user ,self.comment, self.rate

