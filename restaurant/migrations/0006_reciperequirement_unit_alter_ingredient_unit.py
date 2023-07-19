# Generated by Django 4.2.2 on 2023-06-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_ingredient_menuitem_purchase_reciperequirement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciperequirement',
            name='unit',
            field=models.CharField(choices=[('tbsp', 'tbsp'), ('gram', 'Gram'), ('kg', 'KiloGram'), ('mg', 'MiliGram')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('tbsp', 'tbsp'), ('gram', 'Gram'), ('kg', 'KiloGram'), ('mg', 'MiliGram')], max_length=5, null=True),
        ),
    ]
