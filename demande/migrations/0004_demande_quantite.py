# Generated by Django 3.1.7 on 2021-03-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0003_demande_date_demande'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='quantite',
            field=models.IntegerField(default=0),
        ),
    ]
