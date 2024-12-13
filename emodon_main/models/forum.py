# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/forum.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .mood import Mood
# from django.contrib.auth.models import User

class Forum(models.Model):

    mood = models.ForeignKey(Mood, on_delete=models.DO_NOTHING,null=True, related_name='moods' )
    created_at = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')

    # def __str__(self):
    #     return self.get__display()

    class Meta:
        # for admin interface
        verbose_name = "Forum"
        verbose_name_plural = "Forums"
        # setting behavior for the request
        ordering = ['-created_at'] 

    # Validation
    def clean(self):
        mood_choices = Mood.objects.all()
        if self.mood not in mood_choices:
            raise ValidationError(_('This is not a valid choice for your mood'))
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)