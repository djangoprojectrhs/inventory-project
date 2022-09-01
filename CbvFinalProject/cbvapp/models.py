from django.db import models
from django.urls import reverse

# Create your models here.
class Cloth(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    price=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
