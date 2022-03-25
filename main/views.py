from django.contrib.auth import authenticate
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer


def index(request):
    return redirect('/admin')


def invitation(request, invite_code):
    user = request.user
    if invite_code == user.invite_code:
        data = {'ERROR': 'Нельзя ввести собственный инвайт-код.'}
    elif user.invited_by is not None:
        data = {'ERROR': 'Вы уже воспользовались приглашением.'}
    else:
        try:
            inviter = User.objects.get(invite_code=invite_code)
            user.invited_by = inviter
            user.save()
            data = {'message': 'Все прошло успешно'}
        except User.DoesNotExist:
            data = {'ERROR': 'Пользователя не существует'}
    return data


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'user': UserSerializer(user, many=False).data})

    def post(self, request):
        data = request.data
        data2 = invitation(request, data['invite_code'])
        return Response(data2)


class CodeEntry(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        if type(data['code']) is int and len(str(data['code'])) == 4:
            data = {'message': 'код успешно принят'}
        else:
            data = {'ERROR': 'введены некоректные данные'}
        return Response(data)


class AuthenticateUser(APIView):
    def post(self, request):
        user = authenticate(request=request)
        if user is None:
            user = User.objects.create_user(phone_number=request.data["phone_number"], password="")

        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh), 'access': str(refresh.access_token)}
        return Response(data)
