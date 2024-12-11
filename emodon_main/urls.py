# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/urls.py
# Author : Morice
# ---------------------------------------------------------------------------


# from rest_framework.routers import DefaultRouter
# # from .views import ReactionViewSet

# router = DefaultRouter()
# # router.register(r'reactions', ReactionViewSet, basename='reaction') exemple

# urlpatterns = router.urls
from django.urls import path

from .views.forum_view import MoodChoiceListView, ForumListView,ForumDetailView
from .views.reaction_view import EmojiListView,ReactionListView

urlpatterns = [
    path('mood_choices/', MoodChoiceListView.as_view(), name='mood-choices'),  # Endpoint pour MOOD_CHOICE
    path('forums/', ForumListView.as_view(), name='forum-list'),  # Endpoint for forum objects
    path('forums/<int:forum_id>', ForumDetailView.as_view(), name='forum-detail'),  # Endpoint for get_by_id Forum
    path('emoji_choices/', EmojiListView.as_view(), name='emoji-choices'),  # Endpoint pour Emoji_CHOICE
    path('reactions/<int:id>', ReactionListView.as_view(), name='reactions-list'),  # Endpoint for reaction objects
]
