from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .models import User


class EmailModelBackend(object):

    def authenticate(self, email=None, password=None):
        try:
            field = 'email'
            case_insensitive_username_field = '{}__iexact'.format(field)
            user = User._default_manager.get(**{case_insensitive_username_field: email})

            # user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None