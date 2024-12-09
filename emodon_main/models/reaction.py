# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/reaction.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from emodon_main.models.forum import Forum

class Reaction(models.Model):
    
    EMOJI_CHOICES = [
        ('heart', '❤️'),
        ('smile', '😊'),
        ('hugging', '🤗'),
        ('kiss', '😘'),
        ('sparkling_heart', '💖'),
        ('two_hearts', '💕'),
        ('love_letter', '💌'),
        ('rose', '🌹'),
        ('bouquet', '💐'),
        ('blush', '☺️'),
        ('cupid', '💘'),
        ('smiling_face_with_hearts', '🥰'),
        ('heartbeat', '💓'),
        ('revolving_hearts', '💞'),
        ('star_struck', '🤩'),
        ('peace', '✌️'),
        ('praying', '🙏'),
        ('butterfly', '🦋'),
        ('dove', '🕊️'),
        ('sunflower', '🌻'),
        ('rainbow', '🌈'),
        ('sparkles', '✨'),
        ('bear', '🐻'),
        ('panda', '🐼'),
        ('cat_heart_eyes', '😻'),
        ('dog', '🐶'),
        ('stars', '🌟'),
    ]
    
    emoji = models.CharField(max_length=50, choices=EMOJI_CHOICES)
    position_x = models.FloatField()  # X Position
    position_y = models.FloatField()  # Y Position
    created_at = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='reactions' )

    def __str__(self):
        return f"{self.get_emoji_display()} at ({self.position_x}, {self.position_y}) for {self.forum}"
    
    def clean(self):
        if self.emoji not in dict(self.EMOJI_CHOICES):
            raise ValidationError(_('This is not a valid choice from the emoji list'))
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
