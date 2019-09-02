from django.test import TestCase

from catalog.forms import UserForm


class UserFormTest(TestCase):

    def test_UserForm_valid(self):
        form = UserForm(data={"username": 'test_user_name', "first_name": 'testname', "last_name": 'testlname'})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = UserForm(data={"username": '', "first_name": '', "last_name": 'testlname'})
        self.assertFalse(form.is_valid())