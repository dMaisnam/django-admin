# Generated by Django 3.1.4 on 2020-12-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('serial_number', models.CharField(max_length=40, unique=True)),
                ('location', models.CharField(max_length=20, unique=True)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
