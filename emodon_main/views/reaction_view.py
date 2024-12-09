# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/views/reaction_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services.reaction_service import ReactionService
from ..serialyzers.reaction_serialyzers import ReactionSerialyser,EmojiSerialysers

class EmojiListView(APIView):
    # Endpoint to send all available emoji to the front
    def get(self,request):

        emoji_choices = ReactionService.get_emoji_choices()
        serializer = EmojiSerialysers(emoji_choices,many=True)

        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

class ReactionListView(APIView):
    # Endpoint to retrieve all reactions from a forum to the front
    def get(self,request,id):
        reactions, message = ReactionService.get_reactions_by_forum_id(forum_pk=id)

        if reactions is None:
            return Response({'message' : message}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReactionSerialyser(reactions, many=True)

        return Response({'data':serializer.data, 'message':message}, status=status.HTTP_200_OK)
    
    # Endpoint to create a new reaction object.
    def post(self, request,id):

        emoji_choice = request.data.get('emoji_choice')
        pos_x = request.data.get('position_x')
        pos_y = request.data.get('position_y')
        success, reaction_instance, message = ReactionService.create_reaction(
            emoji=emoji_choice,
            position_x=pos_x,
            position_y=pos_y,
            forum_pk=id,
            )
        
        # Serialize the newly created Reaction object
        serializer = ReactionSerialyser(reaction_instance)

        if not success:
            return Response({"message":message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"data":serializer.data, "message":message}, status=status.HTTP_201_CREATED)
    
    # Endpoint to delete the selected forum by id.
    def delete(self, request, id):
        success, message =ReactionService.delete_reaction(id)

        if not success:
            return Response({"message" : message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message" : message}, status=status.HTTP_200_OK)