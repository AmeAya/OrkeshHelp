from django.db import models

# Create your models here.
class HotSprings(models.Model):
    name = models.CharField(max_length=100)
    insta = models.TextField()
    website = models.CharField(max_length=50, null=True, blank=True)
    geoposition = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.name
