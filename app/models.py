from django.db import models

# Create your models here.
class Movie_info(models.Model):
    movie_name=models.CharField(max_length=50)
    movie_review=models.CharField(max_length=50)
    movie_release_date=models.CharField(max_length=50)
    movie_detail=models.TextField(max_length=500)
    movie_hero=models.CharField(max_length=50)
    movie_heroin=models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name