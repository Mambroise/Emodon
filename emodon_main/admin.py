# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/admin.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import admin
from .models import Mood,Emoji

# Register your models here.
admin.site.register(Mood)
admin.site.register(Emoji)
