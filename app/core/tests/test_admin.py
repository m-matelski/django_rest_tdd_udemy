# Admin page unit test

# possibility to test admin
from django.test import TestCase, Client

from django.contrib.auth import get_user_model
# creating url for admin panel
from django.urls import reverse

l = [1, 2, 3]


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='pass123'
        )
        # uses client helper function that allows to log user in with the Django aythentication.
        # It helps with testing because we dont have to manually log in user
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='test2@domain.com',
            password='password123',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Test users are listed in django admin"""
        # reverse - app:url_you_want - defined in django doc
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # Django specific test assertions, checks user in response
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
    
    def test_user_change_page(self):
        """Test that user edit page works"""
        #e g: /admin/core/user/3
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertAlmostEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin"core_user_add')
        res = self.client.get(url)
        self.assertAlmostEqual(res.status_code, 200)

        

