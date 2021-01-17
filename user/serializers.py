from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'last_name', 'first_name')
        # write_only_fields = ('password',)

        extra_kwargs = {
            'password': {'write_only': True}
        }

        read_only_fields = ('id', 'is_admin')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user