from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
# image size restriction
def file_size(value):
    limit = 4 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('video is too large. Video Size should not exceed 4 MB.')

class Categories(models.Model):
    category = models.CharField(max_length=100, )

    def __str__(self):
        return self.category


class Listing(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=300)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex='^\d{11}$', message='invalid number', code='Invalid number')])
    Address = models.CharField(max_length=100)
    Website = models.URLField(max_length=100, null=True, blank=True)
    Category = models.ManyToManyField(Categories)
    Created_at = models.DateTimeField(auto_now_add=True)
    Logo = models.FileField(upload_to='photos/', null=True, blank=True, validators=[file_size])

    def __str__(self):
        return self.Name


class Asset(models.Model):
    Owner = models.ForeignKey(Listing, on_delete="cascade")
    Title = models.CharField(max_length=255, blank=True)
    Image_files = models.FileField(upload_to='photos/', validators=[file_size])
    Uploaded_at = models.DateTimeField(auto_now_add=True)
