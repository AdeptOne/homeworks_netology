from django.db import models


class Phone(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=1)
    image = models.ImageField('Изображение', upload_to='images/')
    release_date = models.DateField()
    lte_exists = models.BooleanField('LTE', default=False)
    slug = models.SlugField()
