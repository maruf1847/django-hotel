# Generated by Django 2.1.5 on 2020-03-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('S', 'Sale'), ('R', 'Rent')], max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=8)),
                ('beds_number', models.PositiveIntegerField()),
                ('baths_number', models.PositiveIntegerField()),
                ('garages_number', models.PositiveIntegerField()),
            ],
        ),
    ]
