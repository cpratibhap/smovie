from rest_framework.routers import SimpleRouter
from movies.views import *
from django.conf.urls import url

routerInstance = SimpleRouter()
routerInstance.register('movies', MovieViewSet)
routerInstance.register('actors', ActorViewSet)
routerInstance.register('director', DirectorViewSet)
routerInstance.register('address', AddressViewSet)


urlpatterns = [
    url('custom/mvactors/', get_movie_actors),
    url('custom/actormvs/', get_allmovies_of_actors),
    url('custom/assign/', assign_movie_to_actors),
    url('custom/assigndir/', assign_director_to_movies),
    url('custom/mvdirector/', get_movie_director),
    url('custom/directormvs/', get_allmovies_of_direcor),
    url('custom/assignaddress/', assign_address_to_actors),
    url('custom/actorsaddress/', get_actors_based_address),
    url('custom/actaddress/', get_actor_address),
    url('custom/assignaddrdir/', assign_address_to_director),
]

urlpatterns += routerInstance.urls

