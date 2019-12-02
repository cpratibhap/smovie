from django.db import models

'''
MOVIE
ACTOR
DIRECTOR
ADDRESS

MOVIE - ACTOR -- M-M
DIRECTOR - MOVIE 1 - M
ACTOR -ADDRESS - M-1
DIRECTOR -ADDRESS - 1-1

'''
# Create your models here.


class Movie(models.Model):
    mvname=models.CharField(max_length=100)
    mvreviews = models.CharField(max_length=100)
    mvcategory = models.CharField(max_length=100)
    active = models.CharField(max_length=2,default='Y')


class Director(models.Model):
    dname = models.CharField(max_length=100)
    dexprc = models.IntegerField()
    active = models.CharField(max_length=2, default='Y')


class Actor(models.Model):
    aname = models.CharField(max_length=100)
    aexprc = models.IntegerField()
    active = models.CharField(max_length=2, default='Y')


class Address(models.Model):
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    active = models.CharField(max_length=2, default='Y')


class MovieActor(models.Model):
    movie = models.ForeignKey('Movie', unique=False, on_delete=models.CASCADE, null=False)
    actor = models.ForeignKey('Actor', unique=False, on_delete=models.CASCADE, null=False)


#1-m
class DirectorMovies(models.Model):
    movie = models.OneToOneField('Movie', unique=True, on_delete=models.CASCADE, null=False)   # many side--unique=True
    director = models.ForeignKey('Director', unique=False, on_delete=models.CASCADE, null=False)    # FK


#m-1
class ActorAddress(models.Model):
    address = models.ForeignKey('Address', unique=False, on_delete=models.CASCADE, null=False)
    actor = models.OneToOneField('Actor', unique=True, on_delete=models.CASCADE, null=False)


class DirectorAddress(models.Model):
    director = models.OneToOneField('Director', unique=True, on_delete=models.CASCADE, null=False)
    address = models.OneToOneField('Address', unique=True, on_delete=models.CASCADE, null=False)
