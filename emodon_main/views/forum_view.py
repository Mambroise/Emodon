# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/views/forum_view.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Forum
from ..services.forum_service import ForumService
from ..serialyzers.forum_serialyzers import ForumSerializer,MoodChoiceSerializer

class MoodChoiceListView(APIView):
    def get(self, request):

        # Endpoint to send all available forums to the front
        mood_choices = [({'key': label, 'value': value}) for label, value in Forum.MOOD_CHOICE]
        serializer = MoodChoiceSerializer(mood_choices, many=True)

        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
    
class ForumListView(APIView):
    def get(self, request):
        
        # Endpoint to send all available forums to the front
        forums = ForumService.read_forum_list()
        serializer = ForumSerializer(forums, many=True)

        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):

        # Endpoint to create a new Forum object based on a mood choice.
        mood_choice = request.data.get('mood_choice')
        
        success, forum_instance, message = ForumService.create_forum(mood_choice)

        # Serialize the newly created Forum object
        serializer = ForumSerializer(forum_instance)

        if not success:
            return Response({"message":message}, status=status.HTTP_400_BAD_REQUEST)


        return Response({"data":serializer.data, "message":message}, status=status.HTTP_201_CREATED)
    
class ForumDetailView(APIView):

    def get(self, request, pk):

        forum, message =ForumService.get_forum_by_id(pk)

        if forum is None:
            return Response({"message" : message}, status=status.HTTP_404_NOT_FOUND)

        serializer = ForumSerializer(forum)

        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)