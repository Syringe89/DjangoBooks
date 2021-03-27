from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from users.forms import CustomUserCreationForm
from users.views import SignupPageView


class CustomUserTests(TestCase):

    def test_create_user(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            username='will',
            email='will@mail.com',
            password='will123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@mail.com')
        self.assertTrue(user.is_active, True)
        self.assertFalse(user.is_staff, False)
        self.assertFalse(user.is_superuser, False)

    def test_create_superuser(self):
        UserModel = get_user_model()
        admin_user = UserModel.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        print(self.response)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        print(view)
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
