# Generated by Django 4.1.2 on 2023-01-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_advert', '0002_rename_inkranya_inkoranya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inkoranya',
            name='description',
            field=models.FileField(upload_to='inkoranya/description'),
        ),
    ]