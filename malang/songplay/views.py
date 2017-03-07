from django.shortcuts import render

import json


from .models import Request,Song,VoteRecord
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q


from django.core import serializers


@csrf_exempt
def index(request):
    
    
    if request.method=='POST':
        

        p = request.POST
        played_song_id = p.get('id_played_request')

        print("this is")
        print(played_song_id)

        if played_song_id:

            played_song_r = Request.objects.get(id=played_song_id)


            played_song_r.played = True
            played_song_r.save()

      
        
        q = Request.objects.filter(played=False).order_by('-upvotes')[0]
        
        next_song_id = q.id   
        next_song_yid = q.youtubeId 
        
        
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



#send a vote for particular request
#after vote is saved in VoteRecord, update vote count in Request



@csrf_exempt
def vote(request):

        print(request.POST)

        post = request.POST
        id = post.get("id")
        downvoted = post.get("down")
        upvoted = post.get("up")


        print(upvoted)


        if downvoted=='false' :

            downvoted = False
        
        elif downvoted=='0' :

            downvoted = False


        else:

            downvoted=True
        


        if upvoted=='false' :
            print("dddhdgg")
            upvoted = False

        elif upvoted== '0' :
            print("dddhdgg")
            upvoted = False

        else:
            print("hiddddddd")
            upvoted=True    



        r = Request.objects.get(id=id)


        if VoteRecord.objects.filter(user=request.user,request=r).exists():

            current_vrec = VoteRecord.objects.get(user=request.user,request=r)
            
            current_upvote = BooleanToInt(current_vrec.upvoted)           
            current_downvote = BooleanToInt(current_vrec.downvoted)

            up_difference  = BooleanToInt(upvoted) - current_upvote
            down_difference  = BooleanToInt(downvoted) - current_downvote

            v = VoteRecord.objects.get(user=request.user,request=r)

            v.upvoted=upvoted
            v.downvoted=downvoted
            v.up_difference =up_difference 
            v.down_difference =down_difference

            v.save()

        elif VoteRecord.objects.filter(user=request.user,request=r).exists()==False:
        

              up_difference =  BooleanToInt(upvoted)
              down_difference = BooleanToInt(downvoted) 
              VoteRecord.objects.create(user=request.user,request=r,upvoted=upvoted,downvoted=downvoted,up_difference =up_difference,down_difference =down_difference)  
                

        
        # print(obj)
        return HttpResponse(request)




# get json array of request objects (id, vote count, upvote status,  vote status) sorted by vote count 

@csrf_exempt
def getTopRequestsJson(request):
    
      
    if request.method=='GET':
    
        request_objects = Request.objects.filter(played=False).extra(select={'offset': 'upvotes - downvotes'}).filter(Q(voterecord__user__username=request.user) | 
                               Q(voterecord__user__username=None)).values('id','song__name','youtubeId','voterecord__upvoted','voterecord__downvoted','voterecord__user__username','offset').order_by('-offset')

        data_dict = ValuesQuerySetToDict(request_objects)
        data_json = json.dumps(data_dict)


        print(data_json)
        # return render(request,"polls/index.html",{"request_objects":request_objects})
    
    return HttpResponse(data_json,content_type='application/json')




@csrf_exempt
def getNewRequestsJson(request):
    
      
    if request.method=='GET':
    
        request_objects = Request.objects.filter(played=False).extra(select={'offset': 'upvotes - downvotes'}).filter(Q(voterecord__user__username=request.user) | 
                               Q(voterecord__user__username=None)).order_by('-added').values('id','song__name','youtubeId','voterecord__upvoted','voterecord__downvoted','voterecord__user__username','offset')

        data_dict = ValuesQuerySetToDict(request_objects)
        data_json = json.dumps(data_dict)


        print(data_json)
        # return render(request,"polls/index.html",{"request_objects":request_objects})
    
    return HttpResponse(data_json,content_type='application/json')







def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

# Usage
# data=MyModel.objects.values('id','title','...','...')
# data_dict = ValuesQuerySetToDict(data)
# data_json = simplejson.dumps(data_dict)


def blankview(request):

    return render(request,'polls/blank.html',{})



def BooleanToInt(x):

    if x==True:
        x=1
        
    elif x==False:
        x=0
        
    return x       

