from django.db import models

# Create your models here.
class blog(models.Model):
    title  = models.CharField(max_length=255)
    kota  = models.CharField(max_length=50)
    provinsi = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='cover/', null=True)

    
    def __str__(self):
        return self.title