# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/mood.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models

class Mood(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.text}"