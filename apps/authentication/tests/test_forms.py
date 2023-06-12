from django.test import TestCase

from apps.authentication.forms import LoginForm, SignUpForm


class FormsTest(TestCase):
    def test_creation_form_not_valid(self):
        form_data = {
            "username": "test",
            "email": "test@test@com",
            "password1": "t1e2s3t4",
            "password2": "t1e2s3t4",
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertNotEqual(form.cleaned_data, form.data)

    def test_creation_form_is_valid(self):

        form_data = {
            "username": "test",
            "email": "test@test.com",
            "password1": "t1e2s3t4",
            "password2": "t1e2s3t4",
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form.data)

    def test_login_form_valid(self):
        form_data = {
            "username": "test",
            "password": "t1e2s3t4",
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_not_valid(self):
        form_data = {
            "username": "test",
            "password": "",
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
