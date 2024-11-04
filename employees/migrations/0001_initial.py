# Generated by Django 5.0.6 on 2024-11-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
