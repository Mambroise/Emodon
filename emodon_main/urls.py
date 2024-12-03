# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/urls.py
# Author : Morice
# ---------------------------------------------------------------------------


from rest_framework.routers import DefaultRouter
# from .views import ReactionViewSet

router = DefaultRouter()
# router.register(r'reactions', ReactionViewSet, basename='reaction') exemple

urlpatterns = router.urls
