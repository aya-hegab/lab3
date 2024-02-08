from django.db import models
from django.shortcuts import reverse
from category.models import *

# Create your models here.
class Product(models.Model):
  name=models.CharField(max_length=100)
  img=models.ImageField(upload_to='products/images', blank=True, null=True)
  category=models.ForeignKey(Category, null=True, blank=True, on_delete= models.CASCADE)

  def __str__(self):
    return self.name
  
  @classmethod
  def productList(self):
    return self.objects.all()
  
  @classmethod
  def productDetails(self, id):
    return self.objects.get(id=id)
  
  def getImageUrl(self):
    return f"/media/{self.img}"
    # return f"{reverse("media")}/{self.img}"