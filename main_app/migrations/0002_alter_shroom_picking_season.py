from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shroom',
            name='picking_season',
            field=models.CharField(choices=[('AZU','Azurescens'), ('CUB','Cubensis'), ('CYA','Cyanescens'), ('SEM','Semilanceata '), ('NAN', 'None')], default='AZU', max_length=3),
        ),
    ]