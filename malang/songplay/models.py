from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import default


#every new song added to library

class Song(models.Model):
    
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100) 

    #rating is the popularity of song on basis of data accumulated 
    # from various online and offline sources
    rating = models.IntegerField()  
    
    
    def __str__(self):
        return self.name
    
    
#every new song request added by a user creates a new row in this table    
    
class Request(models.Model):
          
    song = models.ForeignKey(Song)
    requestee = models.ForeignKey(User)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    youtubeId = models.CharField(max_length=120)
    played = models.BooleanField(default=False)
    
    def __str__(self):
        return self.song.name
    
    
    
#every new song request added by a user creates a new row in this table    
    
class VoteRecord(models.Model):
          
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    
    
    upvoted = models.BooleanField(default=False)
    downvoted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('user', 'request',)
        
    def __str__(self):
        return (self.user.username + '-' + self.request.song.name)
        
        
        