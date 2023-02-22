from django.db import models

# Create your models here.

class Products(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    productDesc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pubDate = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.productName