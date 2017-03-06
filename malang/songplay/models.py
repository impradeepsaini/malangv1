from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import default

from django.db.models.signals import post_save
from django.dispatch import receiver



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
    added = models.DateTimeField(auto_now_add=True)
    played = models.BooleanField(default=False)

    
    
    def __str__(self):
        return self.song.name
    
    
    
#every new song request added by a user creates a new row in this table    
    
class VoteRecord(models.Model):
          
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    
    
    upvoted = models.BooleanField(default=False)
    downvoted = models.BooleanField(default=False)

    up_difference  = models.IntegerField(default=0)
    down_difference  = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('user', 'request',)
        # db_table = 'voterecord'    

    def __str__(self):
        return (self.user.username + '-' + self.request.song.name)
        


@receiver(post_save, sender=VoteRecord, dispatch_uid="update_vote_count")
def update_vote(sender, instance, **kwargs):
     
     r_current_upvotes = instance.request.upvotes
     r_current_downvotes = instance.request.downvotes

     print("r_current_dw")
     print(r_current_downvotes)

     up_difference  = instance.up_difference 
     down_difference  = instance.down_difference 

     print("updifference is-")
     print(up_difference)

     upvotes=r_current_upvotes+up_difference
     downvotes=r_current_downvotes+down_difference


     r = instance.request

     print(r)

     r.upvotes = upvotes
     r.downvotes = downvotes
     r.save()

     #  
     # Request.objects.filter(id=id).update(upvotes=upvotes ,downvotes=downvotes)
     # 
     return 1