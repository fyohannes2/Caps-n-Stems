
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('bloom_season', models.CharField(choices=[('AZU','Azurescens'), ('CUB','Cubensis'), ('CYA','Cyanescens'), ('SEM','Semilanceata ')], default='AZU', max_length=3)),
                ('picking_season', models.CharField(choices=[('AZU','Azurescens'), ('CUB','Cubensis'), ('CYA','Cyanescens'), ('SEM','Semilanceata ')], default='AZU', max_length=3)),
               ('description', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('spread', models.CharField(max_length=100)),
            ],
        ),
    ]