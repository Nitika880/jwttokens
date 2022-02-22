from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email')

    def create(self,validated_data):
        user= User.objects.create(email = validated_data['email'],
                                  username= validated_data['username'],
                                  password= make_password(validated_data['password']),

                                  )
        user.save()
        return user

    def validate_user(self,i):
        # print(f"email{email}")
        # .....
        exclude_list = self.context.get('request').user
        if i in exclude_list:
            raise serializers.ValidationError("We cannot send an email to this user")
        # .....
        return i
    #
    # def validated_username(self,username):


# class NewSerializer(serializers.Serializer):
#     name= serializers.CharField(max_length=10)
