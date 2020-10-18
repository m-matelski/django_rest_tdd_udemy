from django.contrib.auth import get_user_model, authenticate
# whenever you are going to output messages in python its good to pass it through translation system just in case you will need it in future
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


# framework built in serializer that can do with specified fields can convert to db fields and save to db
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    # specify meta - model, fields you wanna include in serializer -
    # these are fields that ll be converted to adn from json when making post requests - accessible fields through api (read/write)
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        # password is write only and has at least 5 characters
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    # validation is checking if our fields are correct

    def validate(self, attrs):
        """Validate and authenticate the user"""
        print(f'{email=} {password=}')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

