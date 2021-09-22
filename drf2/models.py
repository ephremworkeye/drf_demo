from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    in_stock = models.BooleanField()

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
    
