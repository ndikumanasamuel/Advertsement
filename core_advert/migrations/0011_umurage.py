# Generated by Django 4.1.2 on 2023-01-15 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_advert', '0010_ikibonezamvugo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Umurage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.FileField(upload_to='umurage/descriptions')),
            ],
        ),
    ]
