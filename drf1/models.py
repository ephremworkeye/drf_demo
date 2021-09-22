from django.db import models

# Create your models here.
class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.first} {self.last}"