# Generated by Django 5.0.3 on 2024-11-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_advertisement_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
