from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    list_of_invitees = serializers.SerializerMethodField()
    inviter_code = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone_number', 'invite_code', 'invited_by', 'list_of_invitees', 'inviter_code')

    def get_list_of_invitees(self, obj):
        list_of_invitees = User.objects.filter(invited_by=obj).values_list('phone_number', flat=True)
        return list_of_invitees

    def get_inviter_code(self, obj):
        if obj.invited_by is None:
            inviter_code = None
        else:
            inviter_code = obj.invited_by.invite_code
        return inviter_code


class InviteCodeSerializer(serializers.ModelSerializer):
    invite_code = serializers.IntegerField()
