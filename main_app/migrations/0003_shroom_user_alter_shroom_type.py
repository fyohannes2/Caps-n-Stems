
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_alter_shroom_picking_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='shroom',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shroom',
            name='type',
            field=models.CharField(choices=[('Tree', 'Tree'), ('Shrub', 'Shrub'), ('Vine', 'Vine'), ('Perin', 'Perineal'), ('Palm', 'Palm'), ('Annuals', 'Annuals')], default='Tree', max_length=15),
        ),
    ]