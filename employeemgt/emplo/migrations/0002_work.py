# Generated by Django 5.1 on 2024-08-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('dis', models.TextField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
