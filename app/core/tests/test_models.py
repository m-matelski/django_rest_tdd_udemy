from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test creating new user with email is successfull"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password 
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email; for new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@mail.com', 'pass123')
        self.assertTrue(user.is_superuser) # Part of Permission mixin
        self.assertTrue(user.is_staff)