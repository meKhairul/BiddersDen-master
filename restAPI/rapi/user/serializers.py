from rest_framework import serializers
from user.models import User, credentials

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',
                  'phone_number',
                  'email',
                  'address',
                  'username',
                  'password')
        '''extra_kwargs = {
            'password' : {'write_only':True} 
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    '''
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = credentials
        fields = ('username',
                  'password')
        '''extra_kwargs = {
            'password' : {'write_only':True} 
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    '''