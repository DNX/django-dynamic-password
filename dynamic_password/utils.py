from datetime import datetime
import difflib
from django.conf import settings


def get_clean_password(raw_password):
    clean_password = ''
    password_pattern = getattr(settings, 'DYNAMIC_PASSWORD_PATTERN', '<PASSWORD>')
    now = datetime.now()
    dynamic_password = now.strftime(password_pattern)
    diff = difflib.SequenceMatcher(None, raw_password, dynamic_password.replace('<PASSWORD>', ''))
    for block in diff.get_matching_blocks():
        if block[2]:
            clean_password += raw_password[0:block[0]]
    return clean_password
