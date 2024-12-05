from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from .serializer import ProductSerializer,RegisterUserSerializer
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from rest_framework.permissions import IsAuthenticated
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
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