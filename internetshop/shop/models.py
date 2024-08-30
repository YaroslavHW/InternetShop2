from django.db import models

# Create your models here.
class Product(models.Model):
   name = models.CharField(max_length=128)
   description = models.TextField()
   price = models.IntegerField()
   image_url = models.CharField(max_length=256)
   model = models.CharField(max_length=64, null=True, blank=True)
   video_memory = models.FloatField(max_length=16, null=True, blank=True)
   pages_count = models.IntegerField(max_length=96, null=True, blank=True)
   cores_count = models.IntegerField(max_length=16, null=True, blank=True)

   def __str__(self):
      return f'{self.name}'
