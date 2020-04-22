# Generated by Django 3.0.4 on 2020-04-20 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0016_auto_20200420_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.Order'),
        ),
    ]
