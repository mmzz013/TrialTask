from django.test import TestCase
from .models import User


# def activate_invitation(request, invite_code):
#     user = request.user
#     try:
#         inviter = User.objects.get(phone_number=invite_code)


def user_creation(phone):
    try:
        _ = User.objects.get(phone_number=phone)
    except User.DoesNotExist:
        user = User.objects.create(phone_number=phone)
        user.save()
