"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelup.models import Gamer


class GamerView(ViewSet):

    def retrieve(self, request, pk):
      gamer = Gamer.objects.get(pk=pk)
      serializer = GamerSerializer(gamer)
      return Response(serializer.data)


    def list(self, request):
      gamers = Gamer.objects.all()
      serializer = GamerSerializer(gamers, many=True)
      return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        gamer = Gamer.objects.create(
            uid=request.data["uid"],
            bio=request.data["bio"],
        )
        serializer = GamerSerializer(gamer)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        gamer = Gamer.objects.get(pk=pk)
        gamer.uid = request.data["uid"]
        gamer.bio = request.data["bio"]

        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        gamer = Gamer.objects.get(pk=pk)
        gamer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            



class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Gamer
        fields = ('uid', 'bio')
