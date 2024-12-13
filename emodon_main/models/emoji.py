# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/emoji.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models

class Emoji(models.Model):
    icon = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.icon}"