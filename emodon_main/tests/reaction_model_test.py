# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/tests/forum_model_test.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Reaction,Forum


class ReactionModelTest(TestCase):

    def test_create_reaction(self):

        forum = Forum.objects.create(title='depressed')

        reaction = Reaction.objects.create(emoji = 'cat_heart_eyes', position_x = 100, position_y = 50, forum=forum)
        self.assertEqual(reaction.emoji, 'cat_heart_eyes')
        self.assertEqual(reaction.position_x, 100)
        self.assertEqual(reaction.position_y, 50)

    def test_valid_reaction(self):
        forum = Forum.objects.create(title='depressed')

        with self.assertRaises(ValidationError):
            reaction = Reaction.objects.create(emoji = 'invalid_emoji', position_x = 100, position_y = 50, forum=forum)

    def test_cascade_reaction(self):
        forum = Forum.objects.create(title='depressed')

        reaction = Reaction.objects.create(emoji = 'cat_heart_eyes', position_x = 100, position_y = 50, forum=forum)
        reaction = Reaction.objects.create(emoji = 'stars', position_x = 100, position_y = 50, forum=forum)
        forum.delete()
        self.assertEqual(Reaction.objects.count(),0)

    def test_stringify_reaction(self):
        forum = Forum.objects.create(title='depressed')

        reaction = Reaction.objects.create(emoji = 'stars', position_x = 100, position_y = 50, forum=forum)
        self.assertEqual(str(reaction), '🌟 at (100, 50) for I feel depressed')

    def test_all_emoji_reaction(self):
        forum = Forum.objects.create(title='sad')

        for emoji,_ in Reaction.EMOJI_CHOICES:
            reaction = Reaction.objects.create(emoji =emoji, position_x = 100, position_y = 50, forum=forum)
            self.assertEqual(reaction.emoji, emoji)