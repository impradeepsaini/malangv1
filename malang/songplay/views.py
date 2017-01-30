from django.shortcuts import render

import json


from .models import Request,Song
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    
    
    if request.method=='POST':
        
      
        
        q = Request.objects.filter(played=False).order_by('upvotes')[0]
        
        next_song_id = q.id   
        next_song_yid = q.youtubeId 
        
        q.played = True
        q.save()
        
        data = json.dumps([{"nextsong_pk": next_song_id, "nextsong_yid":next_song_yid}])
        return HttpResponse(data,  content_type='application/json')
     
    
    if request.method=='GET':
    
        request_objects = Request.objects.filter(played=False).extra(select={'offset': 'upvotes - downvotes'}).order_by('-offset')
        return render(request,"polls/index.html",{"request_objects":request_objects})
    

# search for youtube videos/songs
def search(request):

        return render(request,"polls/y-search.html",{})  


#add a video/song in request
@csrf_exempt
def add(request):


    if request.method=='POST':


        print(request.POST.get('title'))
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # r = json.loads(request.body)
 
        p =    request.POST    
        title = p.get("title")
        youtubeId = p.get("youtubeId")
        obj, created = Song.objects.get_or_create(name=title,rating=0)



        r = Request(requestee=request.user,song=obj,youtubeId=youtubeId,upvotes=0,downvotes=0)
        r.save();
        # print(body["test"])
 
        return HttpResponse(request.POST)
    
    if request.method=='GET':

        print(request.body[0])    
        return HttpResponse(request)