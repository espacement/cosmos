from django.contrib import admin
from users.models import CustomUser, CustomUserAdmin
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)