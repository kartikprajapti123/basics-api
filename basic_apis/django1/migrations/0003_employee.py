# Generated by Django 4.0 on 2024-01-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django1', '0002_address_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=100)),
            ],
        ),
    ]
