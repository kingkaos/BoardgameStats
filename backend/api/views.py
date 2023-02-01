from django.shortcuts import render, reverse

from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import BoardgameSerializer
from .models import Boardgame

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'boardgames': reverse('boardgame-list', request=request, format=format),
        })


class BoardgameList(generics.ListCreateAPIView):
    queryset = Boardgame.objects.all()
    serializer_class = BoardgameSerializer


@csrf_exempt
def boardgames(request):
    if (request.method == 'GET'):
        boardgames = Boardgame.objects.all()
        serializer = BoardgameSerializer(boardgames, many=True)
        return JsonResponse(serializer.data, safe=False)
