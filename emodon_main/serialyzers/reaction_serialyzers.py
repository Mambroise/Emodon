# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/reaction_serialysers.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework import serializers

from ..models import Reaction

class ReactionSerialyser(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'emoji', 'position_x', 'position_y', 'created_at']

class EmojiSerialysers(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.CharField()