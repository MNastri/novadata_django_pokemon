# Generated by Django 4.1.3 on 2022-11-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="number",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
