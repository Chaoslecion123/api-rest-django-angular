# Generated by Django 2.1.5 on 2019-01-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_portafolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
