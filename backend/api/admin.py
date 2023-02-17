from django.contrib import admin

from .models.boardgame import Boardgame
from .models.stats import Stats
from .models.users import User


admin.site.register(Boardgame)
admin.site.register(Stats)
admin.site.register(User)
