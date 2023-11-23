from django.contrib import admin
from .models import Contact,Service,Comment,News,Team

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','message','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Contact,ContactAdmin)



class ServiceAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','service','city','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')
    
admin.site.register(Service,ServiceAdmin)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('post','name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message') 
    
admin.site.register(Comment,CommentAdmin)

class TeamAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','message','created_date')
    list_filter = ('email',)
    search_fields = ('name','email')
    
admin.site.register(Team,TeamAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)

admin.site.register(News,NewsAdmin)