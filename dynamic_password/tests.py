from datetime import datetime
from django.test import TestCase
from dynamic_password.utils import get_clean_password
from django.test.utils import override_settings
from django.contrib.auth.models import User


class GetCleanPasswordTest(TestCase):

    def setUp(self):
        self.now = datetime.now()

    @override_settings(DYNAMIC_PASSWORD_PATTERN='<PASSWORD>%d')
    def test_get_clean_password_day(self):
        self.assertEqual(get_clean_password(self.now.strftime('denis%d')), 'denis')
        self.assertEqual(get_clean_password(self.now.strftime('apr1%d')), 'apr1')

    @override_settings(DYNAMIC_PASSWORD_PATTERN='%m<PASSWORD>%d')
    def test_get_clean_password_month_day(self):
        self.assertEqual(get_clean_password(self.now.strftime('%msecret%d')), 'secret')
        self.assertEqual(get_clean_password(self.now.strftime('%msec%dret%d')), self.now.strftime('sec%dret'))
        self.assertEqual(get_clean_password(self.now.strftime('secret%d')), '')
        self.assertEqual(get_clean_password('secret'), '')

    @override_settings(DYNAMIC_PASSWORD_PATTERN='%m<PASSWORD>%d.%Y')
    def test_get_clean_password_month_day_year(self):
        self.assertEqual(get_clean_password(self.now.strftime('%ms3c43t%d.%Y')), 's3c43t')
        self.assertEqual(get_clean_password(self.now.strftime('%ms3c43t%d.%Y%d.%Y')), self.now.strftime('s3c43t%d.%Y'))


class DynamicPasswordBackendTest(TestCase):
    fixtures = [
                'user_test',
                ]

    def setUp(self):
        self.now = datetime.now()

    @override_settings(DYNAMIC_PASSWORD_PATTERN='<PASSWORD>')
    def test_login_backend_static(self):
        login = self.client.login(username='test', password='test')
        self.assertTrue(login)
        login = self.client.login(username='test', password='test%s' % self.now.day)
        self.assertFalse(login)

    @override_settings(DYNAMIC_PASSWORD_PATTERN='<PASSWORD>%d')
    def test_login_backend_day(self):
        login = self.client.login(username='test', password='test')
        self.assertFalse(login)
        login = self.client.login(username='test', password=self.now.strftime('test%d'))
        self.assertTrue(login)

    @override_settings(DYNAMIC_PASSWORD_PATTERN='%d<PASSWORD>%m.%Y')
    def test_login_backend_day_month_year(self):
        login = self.client.login(username='test', password='test2012')
        self.assertFalse(login)
        login = self.client.login(username='test', password=self.now.strftime('%dtest%m.%Y'))
        self.assertTrue(login)

    @override_settings(DYNAMIC_PASSWORD_PATTERN='<PASSWORD>%d')
    @override_settings(DYNAMIC_PASSWORD_ONLY_STAFF=True)
    def test_login_backend_only_staff_true(self):
        new_user = User.objects.create_user('newuser', 'newuser@test.com', 'newuserpass')
        login = self.client.login(username='newuser', password='newuserpass')
        self.assertTrue(login)
        login = self.client.login(username='newuser', password=self.now.strftime('newuserpass%d'))
        self.assertFalse(login)
        new_user.is_staff = True
        new_user.save()
        login = self.client.login(username='newuser', password='newuserpass')
        self.assertFalse(login)
        login = self.client.login(username='newuser', password=self.now.strftime('newuserpass%d'))
        self.assertTrue(login)

    @override_settings(DYNAMIC_PASSWORD_PATTERN='<PASSWORD>%d')
    @override_settings(DYNAMIC_PASSWORD_ONLY_STAFF=False)
    def test_login_backend_only_staff_false(self):
        new_user = User.objects.create_user('newuser', 'newuser@test.com', 'newuserpass')
        login = self.client.login(username='newuser', password='newuserpass')
        self.assertFalse(login)
        login = self.client.login(username='newuser', password=self.now.strftime('newuserpass%d'))
        self.assertTrue(login)
        new_user.is_staff = True
        new_user.save()
        login = self.client.login(username='newuser', password='newuserpass')
        self.assertFalse(login)
        login = self.client.login(username='newuser', password=self.now.strftime('newuserpass%d'))
        self.assertTrue(login)
