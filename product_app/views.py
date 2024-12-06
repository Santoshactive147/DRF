from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import * 
from .serializer import ProductSerializer,RegisterUserSerializer,ProductDetailSerializer,ListUserSerializer
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.

from rest_framework.permissions import IsAuthenticated




class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [AllowAny]


   


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    

class ProductCreateDetailView(generics.ListCreateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]


# # Step 2: Create the RegisterUserView class for handling registration requests
# class RegisterUserView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         """
#         Handle the user registration.
#         """
#         serializer = RegisterUserSerializer(data=request.data)

#         # Validate and save the user if the serializer is valid
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(
#                 {
#                     "message": "User registered successfully",
#                     "user": {
#                         "username": user.username,
#                         "email": user.email
#                     }
#                 },
#                 status=status.HTTP_201_CREATED
#             )
        
#         # If serializer is invalid, return validation errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterUserSerializer
from .utils import send_welcome_email  # Import the send_welcome_email function

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle the user registration.
        """
        serializer = RegisterUserSerializer(data=request.data)

        # Validate and save the user if the serializer is valid
        if serializer.is_valid():
            user = serializer.save()
            
            # Send the welcome email after user is created
            send_welcome_email(user.email, user.username)
            
            return Response(
                {
                    "message": "User registered successfully",
                    "user": {
                        "username": user.username,
                        "email": user.email
                    }
                },
                status=status.HTTP_201_CREATED
            )
        
        # If serializer is invalid, return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import logging
from django.http import HttpResponse

# Get the logger for this module
logger = logging.getLogger(__name__)

def my_view(request):
    try:
        # Simulate some logic
        result = 10 / 0  # This will raise a ZeroDivisionError
        return HttpResponse(f"Result: {result}")
    except ZeroDivisionError as e:
        # Log the error with exception details
        logger.error("An error occurred: %s", e, exc_info=True)
        return HttpResponse("An error occurred, check the logs for details.", status=500)


from django.utils.dateparse import parse_date
import logging
class ProductDateRange(APIView):

    def get(self,request,*args,**kwargs):

        from_date_str = request.query_params.get('from_date')
        to_date_str = request.query_params.get('to_date')
       

        logger = logging.getLogger('product_app')
        logger.debug('This is a test DEBUG log message.')
        logger.info('hello this is info ',from_date_str)


        if not from_date_str or not to_date_str:
            return Response({"error": "Both 'from_date' and 'to_date' are required."}, status=status.HTTP_400_BAD_REQUEST)
        from_date = parse_date(from_date_str)
        to_date = parse_date(to_date_str)
        if not from_date or not to_date:
            return Response({"error": "Invalid date format. Please use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

        products = Product.objects.filter(created_at__gte=from_date, created_at__lte=to_date)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)