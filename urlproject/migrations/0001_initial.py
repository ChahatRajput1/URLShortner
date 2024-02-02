# Generated by Django 5.0.1 on 2024-02-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongToShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField(max_length=255)),
                ('shorturl', models.CharField(max_length=50, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
                ('dclicks', models.IntegerField(default=0)),
                ('mclicks', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=100)),
                ('country_count', models.IntegerField(default=0)),
            ],
        ),
    ]
