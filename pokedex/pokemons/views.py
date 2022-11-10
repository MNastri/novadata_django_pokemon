from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from . import models


class PokemonList(ListView):
    model = models.Pokemon


class PokemonDetail(DetailView):
    model = models.Pokemon


class PokemonCreate(LoginRequiredMixin, CreateView):
    model = models.Pokemon
    fields = ["name", "image", "number"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# my_pokemons = [{"name": "ekans"}, {"name": "muk"}]
#
#
# def testview(request):
#     context = {"object_list": my_pokemons}
#     return render(request, template_name="pokemons/pokemons_list.html", context=context)
