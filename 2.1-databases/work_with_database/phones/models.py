from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.FileField(upload_to='goods/')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=64)
