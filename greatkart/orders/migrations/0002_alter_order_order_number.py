# Generated by Django 4.0 on 2022-02-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]