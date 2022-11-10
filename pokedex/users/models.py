import pokemons

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField(pokemons.models.Pokemon, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
