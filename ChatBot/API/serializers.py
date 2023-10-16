from rest_framework import serializers
from API.models import Chat
from API.utils import send_code_to_api
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("id", "_input", "_output")
        extra_kwargs = {
            "_output": {"read_only": True}
        }
    
    def create(self, validated_data):
        _input = validated_data.get("_input")
        _output = send_code_to_api(_input)  # Make sure send_code_to_api is correctly implemented
        validated_data["_output"] = _output

        # Create the Chat model instance
        chat_instance = Chat(**validated_data)
        chat_instance.save()

        return chat_instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password","email")
        extra_kwargs = {
            "password" :{"write_only": True}
        }
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        Token.objects.create(user=user)
        return user
class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(request=self.context.get("request"), username=username, password=password)

        if not user:
            msg = "Unable to authenticate with provided credentials"
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs