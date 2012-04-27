import re
from datetime import datetime
from django.conf import settings


def get_clean_password(raw_password):
    password_pattern = getattr(settings, 'DYNAMIC_PASSWORD_PATTERN', '<PASSWORD>')
    now = datetime.now()
    dynamic_password = now.strftime(password_pattern).replace('<PASSWORD>', '(?P<password>.*)')
    match_result = re.match(dynamic_password, raw_password)
    if match_result:
        return match_result.group('password')
    return ''
