# Generated by Django 4.0.4 on 2022-06-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('city', models.CharField(choices=[('mi', 'mumbai'), ('dl', 'delhi')], max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
