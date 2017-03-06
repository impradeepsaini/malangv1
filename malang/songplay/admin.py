from django.contrib import admin

from .models import Song,Request
from songplay.models import VoteRecord




class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('added',)

# Register your models here.
admin.site.register(Song)
admin.site.register(Request,RatingAdmin)
admin.site.register(VoteRecord)
