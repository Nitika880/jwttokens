from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserCreate(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class detail(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request):
      return Response({"msg":"Success"})


@api_view(['POST','GET'])
def send_email_view(request):
    # .....
    if request.method == "POST":

        # data = JSONParser().parse(request)
        context = {"user_id": request.user.id,"username":request.user.username,"password":request.user.password}

        # context="test@test.com"
        serializer = UserSerializer(data=request.data, context ={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method=="GET":
        queryset=User.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return  Response(serializer.data)