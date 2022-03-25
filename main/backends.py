from django.contrib.auth.backends import ModelBackend
from .models import User


class PasswordlessAuthBackend(ModelBackend):

    def authenticate(self, request):
        try:
            return User.objects.get(phone_number=request.data["phone_number"])
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
