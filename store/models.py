from django.db import models

# Create your models here.
class product(models.Model):
    p_id = models.IntegerField()
    img = models.FileField(upload_to = 'product')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    detail = models.TextField()

    def __str__(self):
        return self.name

class cart(models.Model):
    cust_id = models.IntegerField()
    product_id = models.IntegerField()