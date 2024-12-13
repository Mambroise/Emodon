# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/reaction_serialysers.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework import serializers

from ..models import Reaction,Emoji

class ReactionSerialyser(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'icon', 'position_x', 'position_y', 'created_at']

class EmojiSerialysers(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = ['id', 'icon']