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
from ..serialyzers.forum_serialyzers import ForumSerializer,MoodChoiceSerializer

class MoodChoiceListView(APIView):
    def get(self, request):
        mood_choices = [({'key': label, 'value': value}) for label, value in Forum.MOOD_CHOICE]
        serializer = MoodChoiceSerializer(mood_choices, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ForumListView(APIView):
    def get(self, request):
        forums = Forum.objects.all().order_by('-created_at')
        serializer = ForumSerializer(forums, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Endpoint to create a new Forum object based on a mood choice.
        """
        mood_choice = request.data.get('mood_choice')
        
        # Validate the mood choice
        if mood_choice not in dict(Forum.MOOD_CHOICE).values():
            return Response(
                {"error": "Invalid mood choice."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new Forum object
        forum_instance = Forum(mood_choice=mood_choice)
        forum_instance.save()

        # Serialize the newly created object
        serializer = ForumSerializer(forum_instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)