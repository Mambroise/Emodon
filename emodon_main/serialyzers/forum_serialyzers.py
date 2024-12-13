# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/forum_serialyzers.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework import serializers

from ..models import Forum,Mood

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'mood', 'created_at'] 

class MoodChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['id', 'text'] 
