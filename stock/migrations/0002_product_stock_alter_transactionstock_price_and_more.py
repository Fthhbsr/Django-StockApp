# Generated by Django 4.1.1 on 2022-10-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transactionstock',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='transactionstock',
            name='price_total',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]