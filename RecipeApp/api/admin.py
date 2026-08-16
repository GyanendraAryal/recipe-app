from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name","profile_image")
    search_fields = ("first_name", "last_name")
    ordering = ("id",)


admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
