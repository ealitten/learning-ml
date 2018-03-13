# Generated by Django 2.0.3 on 2018-03-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type_1', models.CharField(blank=True, max_length=50, null=True)),
                ('type_2', models.CharField(blank=True, max_length=50, null=True)),
                ('hp', models.PositiveIntegerField(default=0)),
                ('attack', models.PositiveIntegerField(default=0)),
                ('defense', models.PositiveIntegerField(default=0)),
                ('sp_attack', models.PositiveIntegerField(default=0)),
                ('sp_defense', models.PositiveIntegerField(default=0)),
                ('speed', models.PositiveIntegerField(default=0)),
                ('generation', models.PositiveIntegerField(default=0)),
                ('lengendary', models.BooleanField(default=False)),
            ],
        ),
    ]