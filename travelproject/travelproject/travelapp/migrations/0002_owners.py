# Generated by Django 4.1.3 on 2022-11-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=250)),
                ('pic', models.ImageField(upload_to='pics')),
                ('role', models.TextField()),
            ],
        ),
    ]
