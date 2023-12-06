from userApp.models import User
from userApp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserView(APIView):
    
    def get(self, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response('Test pour pipeline sortie')
    



