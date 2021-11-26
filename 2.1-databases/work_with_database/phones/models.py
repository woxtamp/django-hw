from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    image = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
