# Generated by Django 4.0.6 on 2022-07-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_shroom_picking_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shroom',
            name='type',
            field=models.CharField(choices=[('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe')], default='Psilocybe', max_length=15),
        ),
    ]
