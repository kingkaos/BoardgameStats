from django.shortcuts import render

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .serializers import BoardgameSerializer
from .models import Boardgame

@csrf_exempt
def boardgame(request):
    if(request.method == 'GET'):
        boardgames = Boardgame.objects.all()
        serializer = BoardgameSerializer(boardgames, many=True)
        return JsonResponse(serializer.data, safe=False)
