# Generated by Django 4.0 on 2024-01-23 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('address1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to='django1.address')),
            ],
        ),
    ]
