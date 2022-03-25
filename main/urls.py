from django.urls import path
from .views import index, UserView, CodeEntry, AuthenticateUser

urlpatterns = [
    path('', index),
    path('api/user_info/', UserView.as_view()),
    path('api/code/', CodeEntry.as_view()),
    path('api/auth/', AuthenticateUser.as_view()),
]
