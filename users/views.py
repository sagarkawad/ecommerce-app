from rest_framework.decorators import api_view
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework import status


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
    
    
# def signin(request):
    # get the name/email and check the password in the db
    # check if it matches and return the JWT
    
    
