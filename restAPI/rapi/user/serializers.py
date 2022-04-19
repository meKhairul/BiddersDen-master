
from rest_framework import serializers
from user.models import Product
from user.models import Users
from user.models import Users, File, credentials
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = credentials
        fields = ('username',
                  'password')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('name',
                  'phone_number',
                  'email',
                  'address',
                  'username',
                  'password',)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_name',
                  'product_category',
                  'base_price',
                  'product_defects',
                  'current_price',
                  'recieved_date',
                  'shipping_date',
                  'delivered_date',
                  'isApproved',
                  'seller',
                  'buyer',
                  )


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "_all_"