from django.contrib import admin
from .models import Member
class MenberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'twitter', 'linkedin', 'facebook', 'website')

admin.site.register(Member,MenberAdmin)