"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer


class GamerView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game 
        """
        gamer = Gamer.objects.get(pk=pk)
        serializer = GamerSerializer(gamer)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game 

        Returns:
            Response -- JSON serialized list of game
        """
        gamers = Gamer.objects.all()
        serializer = GamerSerializer(gamers, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized game instance"""
        
        user = Gamer.objects.get(user=request.auth.user)

        gamer = Gamer.objects.create(
            bio=request.data["bio"],
            user=user
        )
        serializer = GamerSerializer(gamer)
        return Response(serializer.data)
    
    

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for gamer
    """
    class Meta:
        model = Gamer
        fields = ('id', 'user', 'bio')
        depth = 1