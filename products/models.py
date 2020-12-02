from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    serial_number = models.CharField(max_length=40, unique=True)
    location = models.CharField(max_length=20, unique=True)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

def _image_upload(instance, filename):
    return f'products/{instance.slug}/{filename}'

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to=_image_upload)

    class Meta:
        ordering = ['order']
        unique_together = ('product', 'order')

    def __str__(self):
        return f'{self.order} for {self.product}'
