# Generated by Django 5.0.3 on 2024-11-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_advertisement_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
