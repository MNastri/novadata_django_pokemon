# Generated by Django 4.1.3 on 2022-11-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemons", "0005_alter_pokemon_name"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="favorites",
            field=models.ManyToManyField(blank=True, to="pokemons.pokemon"),
        ),
    ]