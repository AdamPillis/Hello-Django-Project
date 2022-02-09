from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """To test Item Model"""

    def test_done_defaults_to_false(self):
        """To test done default is set to false"""
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
