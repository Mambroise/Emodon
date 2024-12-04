# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/models/forum.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User

class Forum(models.Model):
    MOOD_CHOICE = [
        ('bad', 'I feel bad'),
        ('alone', 'I feel lonely'),
        ('depressed', 'I feel depressed'),
        ('hard', 'Life is so hard'),
        ('useless', 'I feel useless'),
        ('tired', 'I feel tired'),
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
            raise ValidationError('This is not a valid choice for your mood')
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)