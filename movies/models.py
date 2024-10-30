from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
	name = models.Charfield(max_length=80)


class Person(models.Model):
	name = models.Charfield(max_length=120)


class Job(models.Model):
	name = models.Charfield(max_length=60)


class Movie(models.Model):
	title = models.Charfield(max_length=120)
	overview = models.Textfield()
	release_date = models.datefield()
	running_time = models.Integerfield()
	budget = models.Integerfield(blank=True)
	tmdb_id = models.Integerfield(blank=True)
	revenue = models.Integerfield(blank=True)
	poster_path = models.URLfield(blank=True)
	genres = models.ManyToManyfield(Genre)
	credits = models.ManyToManyfield(Person, through=’MovieCredit’)

class MovieCredit(models.Model):
	person = models-ForeignKey(Person, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)

