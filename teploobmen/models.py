from django.db import models

# Create your models here.
class TeploObmennik(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length = 2083)
# models.py


class Year(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.year)

class ProductCard(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='product_cards')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title
