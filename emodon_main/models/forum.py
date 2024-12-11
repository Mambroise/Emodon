# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/forum.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User

class Forum(models.Model):
    MOOD_CHOICE = [
        ('bad', _('I feel bad')),
        ('alone', _('I feel lonely')),
        ('depressed', _('I feel depressed')),
        ('hard', _('Life is so hard')),
        ('useless', _('I feel useless')),
        ('tired', _('I feel tired')),
        ('sad', _('I feel sad')),
    ]

    title = models.CharField(max_length=50, choices=MOOD_CHOICE)
    created_at = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')

    def __str__(self):
        return self.get_title_display()

    class Meta:
        # for admin interface
        verbose_name = "Forum"
        verbose_name_plural = "Forums"
        # setting behavior for the request
        ordering = ['-created_at'] 

    # Validation
    def clean(self):
        if self.title not in dict(self.MOOD_CHOICE):
            raise ValidationError(_('This is not a valid choice for your mood'))
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)