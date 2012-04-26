from django.conf import settings
from django.contrib.auth.models import User
from dynamic_password.utils import get_clean_password


class DynamicPasswordBackend(object):
    """
    Authenticate against the settings DYNAMIC_PASSWORD_PATTERN and DYNAMIC_PASSWORD_ONLY_STAFF.

    Set DYNAMIC_PASSWORD_PATTERN in your settings.py. For example:

    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD><dd>'
    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD><dd>'
    DYNAMIC_PASSWORD_PATTERN = '<mm><PASSWORD><dd>'
    DYNAMIC_PASSWORD_PATTERN = '<dd><PASSWORD><yy>'
    """

    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        password = get_clean_password(password)
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
