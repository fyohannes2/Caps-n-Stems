from django.db import models

# Create your models here.

# Add the Cat class & list and view function below the imports
class Shroom:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, scientific_name, family, bloom_season, picking_season, height, spread, description):
        self.name = name
        self.scientific_name = scientific_name
        self.family = family
        self.bloom_season = bloom_season
        self.picking_season = picking_season
        self.description = description
        self.height = height
        self.spread = spread

shrooms = [
    Shroom('Japanese Maple', 'Acer Palmatum', 'Sapinaceae', 'Sping', None, '15 - 25ft', '10 - 15ft', 'Looks goooood'),
    Shroom('Maple', 'Acer Palmatum', 'Sapinaceae', 'Sping', None, '15 - 25ft', '10 - 15ft', 'Looks goooood'),
    Shroom('Japanese', 'Acer Palmatum', 'Sapinaceae', 'Sping', None, '15 - 25ft', '10 - 15ft', 'Looks goooood'),
] 
