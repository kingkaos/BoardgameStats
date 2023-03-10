from rest_framework import routers, serializers, viewsets
from .models.boardgame import  Boardgame
from .models.stats import Stats
from .models.users import User


class BoardgameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        app_label = 'boardgame'
        model = Boardgame
        fields = [
            'id', 
            'title', 
            'description'
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        app_label = 'user'
        model = User
        fields = ['id', 'nick_name']


class StatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        app_label = 'stats'
        model = Stats
        fields = ['id', 'played_on']
