from rest_framework import routers, serializers, viewsets
from .models.boardgame import  Boardgame


class BoardgameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        app_label = 'boardgame'
        model = Boardgame
        fields = ['id', 'title', 'description']
