from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(default="default_missingno.png", upload_to="pokemon_pics")
    number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pokemons-detail", kwargs={"pk": self.pk})
