# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/forum_serialyzers.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework import serializers

from ..models import Forum

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'title', 'created_at'] 

class MoodChoiceSerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.CharField()
