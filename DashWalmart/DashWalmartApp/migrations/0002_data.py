# Generated by Django 3.2.12 on 2022-03-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashWalmartApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store', models.IntegerField()),
                ('Dept', models.IntegerField()),
                ('Weekly_Sales', models.FloatField()),
            ],
        ),
    ]
