from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(default="default_missingno.png", upload_to="pokemon_pics")
    number = models.PositiveIntegerField(unique=True)
    hp = models.PositiveIntegerField(verbose_name="Hit Points")
    attack = models.PositiveIntegerField()
    defense = models.PositiveIntegerField()
    sp_atk = models.PositiveIntegerField(verbose_name="Special Attack")
    sp_def = models.PositiveIntegerField(verbose_name="Special Defense")
    speed = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pokemons-detail", kwargs={"pk": self.pk})
