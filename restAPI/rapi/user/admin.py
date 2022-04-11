from django.contrib import admin

from user.views import user

from user.models import User

# Register your models here.

admin.site.register(User)