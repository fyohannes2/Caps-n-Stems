from django.db import models
from django.urls import reverse

# Create your models here.

SPECIES = (
    ('AZU','Azurescens'),
    ('CUB','Cubensis'),
    ('CYA','Cyanescens'),
    ('SEM','Semilanceata ')
)
SPECIEZ = (
    ('AZU','Azurescens'),
    ('CUB','Cubensis'),
    ('CYA','Cyanescens'),
    ('SEM','Semilanceata ')
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
        choices=SPECIES,
        default= SPECIES[0][0],)
    picking_season = models.CharField(
        max_length=3,
        choices=SPECIEZ,
        default= SPECIEZ[0][0],)
    description = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shroom_id': self.id})
