import pokemons

from django.contrib.auth.models import User
from django.db import models

from . import signals


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField(pokemons.models.Pokemon, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def create_user_profile(self, sender, instance, created, **kwargs):
        signals.create_profile(sender, instance, created, **kwargs)

    def save_user_profile(self, sender, instance, **kwargs):
        signals.save_profile(sender, instance, **kwargs)
