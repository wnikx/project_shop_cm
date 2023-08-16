from django.db import models
from datetime import date


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


class Product(models.Model):
    LITER = "л"
    KILOGGRAM = "кг"
    MEASURMENT_UNIT_CHOICES = [
        (LITER, 'литр'),
        (KILOGGRAM, 'килограмм'),
    ]

    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    min_volume = models.DecimalField(max_digits=2,
                                     decimal_places=1)
    unit = models.CharField(max_length=2,
                            choices=MEASURMENT_UNIT_CHOICES, default=KILOGGRAM)
    available = models.BooleanField(default=True)
    create = models.DateField(default=date.today)
