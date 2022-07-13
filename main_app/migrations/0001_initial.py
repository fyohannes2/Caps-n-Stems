# Generated by Django 4.0.6 on 2022-07-13 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe'), ('Psilocybe', 'Psilocybe')], default='Psilocybe', max_length=15)),
                ('bloom_season', models.CharField(choices=[('SUM', 'Summer'), ('SPG', 'Spring'), ('FLL', 'Fall'), ('WIN', 'Winter')], default='SUM', max_length=3)),
                ('picking_season', models.CharField(choices=[('SUM', 'Summer'), ('SPG', 'Spring'), ('FLL', 'Fall'), ('WIN', 'Winter'), ('NAN', 'None')], default='SUM', max_length=3)),
                ('description', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('spread', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
