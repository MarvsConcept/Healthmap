# from django.contrib.gis.db import models

# class Hospital(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     location = models.PointField()
#     contact_number = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# # hospitals/models.py


from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator, MaxValueValidator

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location = gis_models.PointField(geography=True, null=True, blank=True, spatial_index=True)
    amenity = models.CharField(max_length=50, blank=True)
    opening_hours = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='hospital_images/', null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude)
        super(Hospital, self).save(*args, **kwargs)

    def __str__(self):
        return self.name