# Generated by Django 3.2.12 on 2022-02-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0002_alter_recipe_cooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
