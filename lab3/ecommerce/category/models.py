from django.db import models

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=100)
  img=models.ImageField(upload_to='category/images', blank=True, null=True)

  def __str__(self):
    return self.name
  
  @classmethod
  def getCategory(self):
    return [(cat.id, cat.name) for cat in self.objects.all()]
    
