# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/reaction.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from emodon_main.models import Forum,Emoji

class Reaction(models.Model):
    

    
    icon = models.ForeignKey(Emoji,on_delete=models.DO_NOTHING,null=True,related_name='icons')
    position_x = models.FloatField()  # X Position
    position_y = models.FloatField()  # Y Position
    created_at = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='reactions' )

    def __str__(self):
        return f"{self.get_icon_display()} at ({self.position_x}, {self.position_y}) for {self.forum}"
    
    def clean(self):
        emoji_choices = Emoji.objects.all()
        if self.icon not in emoji_choices:
            raise ValidationError(_('This is not a valid choice from the emoji list'))
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
