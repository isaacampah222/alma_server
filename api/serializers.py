from rest_framework import serializers
from .models import SingleOrder,UserProfile

class SingleOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SingleOrder
        fields = ['id','customer_id','order_id','order_string']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','username', 'email','phone_number')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','username','password','email')
        extra_kwargs = {'password':{'write_only': True}}

        def create(self, validated_data):
            user = UserProfile.objects.create_user(validated_data['username'],validated_data['password'],validated_data['email'],validated_data['phone'])

            return user