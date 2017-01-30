from django.contrib import admin

from .models import Song,Request
from songplay.models import VoteRecord


# Register your models here.
admin.site.register(Song)
admin.site.register(Request)
admin.site.register(VoteRecord)
