from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """class created to test item form"""
    def test_item_name_is_required(self):
        """testing if name is required"""
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """testing if done is not required"""
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """testing if name and done only show within the form and to the user"""
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
