from django.test import TestCase
from dynamic_password.utils import get_clean_password


class DynamicPasswordTest(TestCase):
    def test_get_clean_password(self):
        self.assertEqual(get_clean_password('denis85'), 'denis')
