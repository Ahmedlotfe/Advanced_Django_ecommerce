# Generated by Django 4.0 on 2022-02-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('orders', '0008_remove_orderproduct_color_remove_orderproduct_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
