# Generated by Django 3.1.7 on 2021-03-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0002_auto_20210324_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='date_demande',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
