from datetime import datetime
from django.test import TestCase
from dynamic_password.utils import get_clean_password
from django.test.utils import override_settings


class DynamicPasswordTest(TestCase):
    def setUp(self):
        self.now = datetime.now()

    @override_settings(DYNAMIC_PASSWORD_PATTERN='<PASSWORD>%d')
    def test_get_clean_password(self):
        self.assertEqual(get_clean_password(self.now.strftime('denis%d')), 'denis')
        self.assertEqual(get_clean_password(self.now.strftime('apr1%d')), 'apr1')
