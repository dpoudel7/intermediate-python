from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)


"""
Instructor notes for all model fields:

- CharField: A string field with a maximum length.
- IntegerField: An integer field.
- TextField: A large text field. blank=True, null=True
- ImageField: An image field.
- DecimalField: A decimal field.
- DateField: A date field.
- DateTimeField: A date and time field.
- BooleanField: A boolean field.

"""