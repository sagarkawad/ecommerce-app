from rest_framework.decorators import api_view
from .serializers import SignupSerializer, SigninSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.
@api_view(["POST"])
def signup(request):
    #1. initialize the serializer with incoming request data
    serializer = SignupSerializer(data=request.data)

    #2. Validate incoming data
    if serializer.is_valid():

        #3. Save user to database
        user = serializer.save()

        #4. Return success response
        return Response(
            {
                "message": "User created successfully",
                "user_id": user.id,
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(["POST"])
def signin(request):
    serializer = SigninSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

   
        user = User.objects.filter(email__iexact=email).first()

        if user is None:
            return Response(
                {
                    "message": "User not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        authenticated_user = authenticate(request, username=user.username, password=password)

        if authenticated_user is None:
            return Response({
                "message": "Invalid Credentials"
            },
            status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(authenticated_user)

        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            "message": "Sign in successful",
            "access_token": access_token,
           "refresh_token": refresh_token 
        }, 
        status=status.HTTP_200_OK
        )
    else:
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
            

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email
    })
    
        
    
    
# def signin(request):
    # get the name/email and check the password in the db
    # check if it matches and return the JWT
    
    
