from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


SEASONS = (
    ('SUM','Summer'),
    ('SPG','Spring'),
    ('FLL','Fall'),
    ('WIN','Winter')
)
SEASONZ = (
    ('SUM','Summer'),
    ('SPG','Spring'),
    ('FLL','Fall'),
    ('WIN','Winter'),
    ('NAN','None'),
)
TYPE = (
    ('Psilocybe','Psilocybe'),
    ('Psilocybe','Psilocybe'),
    ('Psilocybe','Psilocybe'),
    ('Psilocybe','Psilocybe'),
    ('Psilocybe','Psilocybe'),
    ('Psilocybe','Psilocybe'),
)

class Shroom(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=15,
        choices=TYPE,
        default= TYPE[0][0],)
    bloom_season = models.CharField(
        max_length=3,
        choices=SEASONS,
        default= SEASONS[0][0],)
    picking_season = models.CharField(
        max_length=3,
        choices=SEASONZ,
        default= SEASONZ[0][0],)
    description = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

   
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shroom_id': self.id})