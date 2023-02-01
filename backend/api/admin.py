from django.contrib import admin

from .models.boardgame import Boardgame
from .models.users import User

# Register your models here.

admin.site.register(Boardgame)
admin.site.register(User)
