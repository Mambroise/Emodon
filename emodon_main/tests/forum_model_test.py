# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/tests/forum_model_test.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models.forum import Forum

class ForumModelTest(TestCase):

    def test_create_forum (self):
        forum = Forum.objects.create(title='alone')
        self.assertEqual(forum.title, 'alone')
    
    def test_invalid_title(self):
        with self.assertRaises(ValidationError):
            forum = Forum.objects.create(title='invalid_title')

    def test_delete_forum(self):
        forum = Forum.objects.create(title='alone')
        forum.delete()
        self.assertEqual(Forum.objects.count(),0)

    def test_stringify_forum(self):
        forum = Forum.objects.create(title='alone')

        self.assertEqual(str(forum), 'I feel lonely')

    def test_all_mood_forum(self):
        for mood, _ in Forum.MOOD_CHOICE:
            forum = Forum.objects.create(title=mood)
            self.assertEqual(forum.title, mood)

    
