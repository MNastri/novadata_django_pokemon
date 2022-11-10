from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from users.models import Profile

from . import models


class PokemonList(ListView):
    model = models.Pokemon
    ordering = "number"


class PokemonDetail(DetailView):
    model = models.Pokemon


class PokemonCreate(LoginRequiredMixin, CreateView):
    model = models.Pokemon
    fields = [
        "name",
        "image",
        "number",
        "hp",
        "attack",
        "defense",
        "sp_atk",
        "sp_def",
        "speed",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def favourite_pokemon(request, pk):
    fav_pokemon = get_object_or_404(models.Pokemon, pk=pk)
    cur_profile = Profile.objects.get(user_id=request.user.id)
    cur_profile.favourites.add(fav_pokemon)
    success_message = f"{fav_pokemon} marked as favourite"
    messages.success(request, success_message)
    return redirect("pokemons-home")


def unfavourite_pokemon(request, pk):
    fav_pokemon = get_object_or_404(models.Pokemon, pk=pk)
    cur_profile = Profile.objects.get(user_id=request.user.id)
    cur_profile.favourites.remove(fav_pokemon)
    success_message = f"{fav_pokemon} unmarked as favourite"
    messages.success(request, success_message)
    return redirect("pokemons-home")
