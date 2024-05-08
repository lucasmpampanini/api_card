from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from user_authenticate.serializers import UserSerializer

class CreateUserView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name='username', description='Nome de usuário', required=True),
            OpenApiParameter(name='password', description='Senha', required=True),
        ],
        responses={200: UserSerializer(many=False)},
        description="Cria um novo usuário",
        summary="Cria um novo usuário",
        operation_id='create_user',
        tags=['Usuários'],
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)