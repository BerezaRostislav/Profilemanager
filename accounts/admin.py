from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name','date_of_birth','contacts','gender']
    search_fields = ['name']

class Meta:
    model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)

