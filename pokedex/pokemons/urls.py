from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.PokemonList.as_view(), name="pokemons-home"),
    path(
        "pokemon/<int:pk>/",
        views.PokemonDetail.as_view(),
        name="pokemons-detail",
    ),
    path(
        "pokemon/<int:pk>/favourite",
        views.favourite_pokemon,
        name="pokemons-favourite",
    ),
    path(
        "pokemon/<int:pk>/unfavourite",
        views.unfavourite_pokemon,
        name="pokemons-unfavourite",
    ),
    path(
        "pokemon/new/",
        views.PokemonCreate.as_view(),
        name="pokemons-create",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
