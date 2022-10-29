from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   age = models.IntegerField() 
   
   def __str__(self):
       return self.last_name + "\n" + self.first_name
   
class Song(models.Model):
    #foreign key from Artiste
    title = models.CharField(max_length=30)
    date_released = models.DateField()
    likes = models.IntegerField(null=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name='song')
    
    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    #foreign key from Song
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='lyric')
    
    def __str__(self):
        return self.content