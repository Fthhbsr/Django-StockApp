# Generated by Django 4.1.1 on 2022-10-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_category_options_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionstock',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
