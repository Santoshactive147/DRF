


# from rest_framework import serializers
# from .models import Product, ProductDetail

# class ProductDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductDetail
#         fields = ['id', 'product', 'warranty_period', 'specifications', 'weight', 'manufacturer']
    
   

# class ProductSerializer(serializers.ModelSerializer):
#     # Nested serializer for ProductDetail
#     manufacturer = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'created_at', 'updated_at', 'manufacturer']

    
#     def get_manufacturer(self,obj):


#             return {
#                 "manufacturer : ": obj.manufacturer.manufacturer
#             }

from rest_framework import serializers
from .models import Product, ProductDetail



class ProductSerializer(serializers.ModelSerializer):
    # Using SerializerMethodField to get manufacturer from the related ProductDetail
    manufacturer = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'created_at', 'updated_at', 'manufacturer']

    def get_manufacturer(self, obj):
        # Get the related ProductDetail and access the manufacturer field
        if hasattr(obj, 'detail'):
            return obj.detail.manufacturer
        return None  # If no ProductDetail exists, return None



class ProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductDetail
        fields = ['id',  'warranty_period', 'specifications', 'weight', 'manufacturer','product']



from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

# Step 1: Create the User registration serializer
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        """
        Ensure that the password and confirm_password match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        """
        Create a new user and return the user instance.
        """
        # Remove confirm_password from validated_data, we don't store it in the database
        validated_data.pop('confirm_password')
        
        # Create the user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"