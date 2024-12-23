# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/views/forum_view.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services.forum_service import ForumService
from ..serialyzers.forum_serialyzers import ForumSerializer,MoodChoiceSerializer

class MoodChoiceListView(APIView):
    # Endpoint to send all available forums to the front
    def get(self, request):

        mood_choices = ForumService.get_mood_choices()
        serializer = MoodChoiceSerializer(mood_choices, many=True)

        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
    
class ForumListView(APIView):
    # Endpoint to send all available forums to the front
    def get(self, request):
        
        forums = ForumService.read_forum_list()
        serializer = ForumSerializer(forums, many=True)

        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
    
    # Endpoint to create a new Forum object based on a mood choice.
    def post(self, request):

        mood_choice = request.data.get('mood_choice')
        success, forum_instance, message = ForumService.create_forum(mood_choice)

        # Serialize the newly created Forum object
        serializer = ForumSerializer(forum_instance)

        if not success:
            return Response({"message":message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"data":serializer.data, "message":message}, status=status.HTTP_201_CREATED)
    

class ForumDetailView(APIView):
    # Endpoint to retrieve the selected forum by id.
    def get(self, request, forum_id):

        forum, message =ForumService.get_forum_by_id(forum_id)

        if forum is None:
            return Response({"message" : message}, status=status.HTTP_404_NOT_FOUND)

        serializer = ForumSerializer(forum)

        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
    

    # Endpoint to delete the selected forum by id.
    def delete(self, request, forum_id):
        success, message =ForumService.delete_forum(forum_id)

        if not success:
            return Response({"message" : message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message" : message}, status=status.HTTP_200_OK)