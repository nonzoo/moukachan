from django.contrib import admin
from .models import Userprofile, State

@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_vendor', 'company_address', 'website']
    list_filter = ['is_vendor']

admin.site.register(State)
