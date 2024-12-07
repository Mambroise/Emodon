# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
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
from .views.forum_view import MoodChoiceListView, ForumListView

urlpatterns = [
    path('mood_choices/', MoodChoiceListView.as_view(), name='mood-choices'),  # Endpoint pour MOOD_CHOICE
    path('forums/', ForumListView.as_view(), name='forum-list'),  # Endpoint pour les objets Forum
]
