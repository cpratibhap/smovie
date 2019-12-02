from django.shortcuts import render
import json
from rest_framework.viewsets import ModelViewSet
from movies.serialization import *
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_swagger import renderers
from rest_framework.decorators import api_view, renderer_classes
from django.http.response import HttpResponse
from django.contrib.auth.models import User


def provide_tokens_tothe_user(req):
    #req.data

    #write a code to check username and password with database
    #in case correct one-- the fetch user token from auth_authtoken

    return HttpResponse("13878b9341c6fd740240d278ff2969400521a92c")


def verify_mandatory_fields(data):
    mandatoryfields = ["movieid","actorids"]
    notavlbfields = []
    for item in mandatoryfields:
        if not data.__contains__(item):
            notavlbfields.append(item)

    if len(notavlbfields)==0:
        return True
    return notavlbfields


@api_view(['POST'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def assign_movie_to_actors(req):
    print('inside assign', req.data)
    result = verify_mandatory_fields(req.data)
    if result==True:
        movieId= req.data.get("movieid")
        actorsIds = req.data.get("actorids")
        mvinstance = Movie.objects.get(id=movieId)
        for actid in actorsIds:
            mvact = MovieActor(movie=mvinstance, actor=Actor.objects.get(id=actid))
            mvact.save()
        return HttpResponse("Success")

    return HttpResponse(json.dumps(result))


@api_view(['GET',"POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_allmovies_of_actors(req):
    print('inside getallmovies')
    allmovieactorsinfo = MovieActor.objects.all()
    moviesList = []
    for movieinfo in allmovieactorsinfo:#1 111  991
        if movieinfo.actor.id==req.data["id"]:
        # if movieinfo.actor.id:
            #instance = Movie.objects.get(id=movieinfo.movie.id)
            instance = movieinfo.movie
            instance.__dict__.pop('_state')
            moviesList.append(instance.__dict__)
    print(moviesList)
    return HttpResponse(json.dumps(moviesList), content_type='application/json')


@api_view(['GET',"POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_movie_actors(req):
    allmovieactorsinfo = MovieActor.objects.all()
    actorsList = []
    for movieinfo in allmovieactorsinfo:#1 111  991
        if movieinfo.movie.id==req.data["id"]:
            #instance = Actor.objects.get(id=movieinfo.actor.id)
            instance = movieinfo.actor
            instance.__dict__.pop('_state')
            actorsList.append(instance.__dict__)
    print(actorsList)
    return HttpResponse(json.dumps(actorsList), content_type='application/json')


def dir_verify_mandatory_fields(data):
    mandatoryfields = ["movieid","directorid"]
    notavlbfields = []
    for item in mandatoryfields:
        if not data.__contains__(item):
            notavlbfields.append(item)

    if len(notavlbfields) == 0:
        return True
    return notavlbfields


@api_view(['POST'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def assign_director_to_movies(req):
    print('inside getdirector')
    print('inside assign director', req.data)
    result = dir_verify_mandatory_fields(req.data)
    if result == True:
        movieIds = req.data.get("movieid")
        directorId = req.data.get("directorid")
        mvinstance = Movie.objects.get(id=movieIds)
        mvdirect = DirectorMovies(movie=mvinstance, director=Director.objects.get(id=directorId))
        mvdirect.save()
        return HttpResponse("Success")

    return HttpResponse(json.dumps(result))


@api_view(['GET',"POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_allmovies_of_direcor(req):
    print('inside getallmovies')
    allmoviedirectorsinfo = DirectorMovies.objects.all()
    moviesList = []
    for movieinfo in allmoviedirectorsinfo:#1 111  991
        if movieinfo.director.id==req.data["id"]:
        # if movieinfo.actor.id:
            #instance = Movie.objects.get(id=movieinfo.movie.id)
            instance = movieinfo.movie
            instance.__dict__.pop('_state')
            moviesList.append(instance.__dict__)
    print(moviesList)
    return HttpResponse(json.dumps(moviesList), content_type='application/json')


@api_view(['GET',"POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_movie_director(req):
    allmoviedirectorsinfo = DirectorMovies.objects.all()
    # directorsList = []
    for movieinfo in allmoviedirectorsinfo:#1 111  991
        if movieinfo.movie.id==req.data["id"]:
            #instance = Actor.objects.get(id=movieinfo.actor.id)
            instance = movieinfo.director
            instance.__dict__.pop('_state')
            # actorsList.append(instance.__dict__)
    # print(actorsList)
    return HttpResponse(json.dumps(instance.__dict__), content_type='application/json')


# RESTRICTED_ACTIONS = ('create', 'update', 'partial_update', 'destroy')
RESTRICTED_ACTIONS = 'partial_update'


def address_verify_mandatory_fields(data):
    mandatoryfields = ["addressid","actorids"]
    notavlbfields = []
    for item in mandatoryfields:
        if not data.__contains__(item):
            notavlbfields.append(item)

    if len(notavlbfields)==0:
        return True
    return notavlbfields


@api_view(['POST'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def assign_address_to_actors(req):
    print('inside assign address',req.data)
    result = address_verify_mandatory_fields(req.data)
    if result==True:
        addressId = req.data.get("addressid")
        actorsIds = req.data.get("actorids")
        addrinstance = Address.objects.get(id=addressId)
        for actid in actorsIds:
            addract = ActorAddress(address=addrinstance,actor=Actor.objects.get(id=actid))
            addract.save()
        return HttpResponse("Success")

    return HttpResponse(json.dumps(result))


@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_actors_based_address(req):
    allactorsaddressinfo = ActorAddress.objects.all()
    actorsList = []
    for actinfo in allactorsaddressinfo:
        if actinfo.address.id==req.data["id"]:
            instance = actinfo.actor
            instance.__dict__.pop('_state')
            actorsList.append(instance.__dict__)

    return HttpResponse(json.dumps(actorsList), content_type='application/json')


@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_actor_address(req):
    allactorsaddressinfo = ActorAddress.objects.all()
    for addressinfo in allactorsaddressinfo:
        if addressinfo.actor.id==req.data["id"]:
            instance = addressinfo.address
            instance.__dict__.pop('_state')

    return HttpResponse(json.dumps(instance.__dict__), content_type='application/json')


def add_dir_verify_mandatory_fields(data):
    mandatoryfields = ["addressid","directorid"]
    notavlbfields = []
    for item in mandatoryfields:
        if not data.__contains__(item):
            notavlbfields.append(item)

    if len(notavlbfields)==0:
        return True
    return notavlbfields


@api_view(['POST'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def assign_address_to_director(req):
    print('inside assign address to director',req.data)
    result = add_dir_verify_mandatory_fields(req.data)
    if result==True:
        addressId = req.data.get("addressid")
        directorsId = req.data.get("directorid")
        addrinstance = Address.objects.get(id=addressId)
        for did in directorsId:
            addrdirect = DirectorAddress(address=addrinstance,director=Director.objects.get(id=did))
            addrdirect.save()
        return HttpResponse("Success")

    return HttpResponse(json.dumps(result))


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.action in RESTRICTED_ACTIONS:
            self.permission_classes = (IsAuthenticated,)
        return super(self.__class__, self).get_permissions()


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_permissions(self):
        if self.action in RESTRICTED_ACTIONS:
            self.permission_classes = (IsAuthenticated,)
        return super(self.__class__, self).get_permissions()


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_permissions(self):
        if self.action in RESTRICTED_ACTIONS:
            self.permission_classes = (IsAuthenticated,)
        return super(self.__class__, self).get_permissions()


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_permissions(self):
        if self.action in RESTRICTED_ACTIONS:
            self.permission_classes = (IsAuthenticated,)
        return super(self.__class__, self).get_permissions()
