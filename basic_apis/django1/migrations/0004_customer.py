# Generated by Django 4.0 on 2024-01-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django1', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users', models.OneToOneField(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='django1.user')),
            ],
        ),
    ]
