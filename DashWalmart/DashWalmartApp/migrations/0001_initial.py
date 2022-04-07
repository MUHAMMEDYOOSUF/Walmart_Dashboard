# Generated by Django 3.2.12 on 2022-03-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_ml',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('fuel', models.FloatField()),
                ('cpi', models.FloatField()),
                ('unemp', models.FloatField()),
                ('week', models.IntegerField()),
                ('ishol', models.IntegerField()),
                ('store', models.IntegerField()),
                ('dept', models.IntegerField()),
                ('typ', models.IntegerField()),
                ('size', models.IntegerField()),
                ('pred', models.FloatField(blank=True)),
            ],
        ),
    ]
