from django.contrib import admin

# Register your models here.
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['email', 'display_name', 'profile_picture']

    def has_add_permission(self, request):
        return False

admin.site.register(CustomUser, CustomUserAdmin)

