from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
import hashlib

from card.serializers import CardSerializer, CardResponse200, CardRequestBody, CardValidationResponse200
from card.models import Card


class CardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='card_number', description='Numero do cartão', required=False),
            OpenApiParameter(name='file_cards', description='Arquivo TXT contendo os cartões', required=False),
        ],
        request=CardRequestBody,
        responses={200: CardResponse200},
        methods=['POST'],
        description="Endpoint para inserir um único cartão ou vários cartões a partir de um arquivo TXT",
    )
    def post(self, request):
        if 'card_number' in request.data:
            serializer = CardSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "ok"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif 'file_cards' in request.FILES:
            file_cards = request.FILES['file_cards']
            for linha in file_cards:
                linha = linha.decode('utf-8').strip()
                if linha.startswith('C'):
                    card_number = linha[8:26].strip()
                    card = Card(card_number=card_number)
                    card.save()
            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    
    

class CardValidationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='card_number', description='Numero do cartão', required=True),
        ],
        request=CardRequestBody,
        responses={200: CardValidationResponse200},
        methods=['POST'],
        description="Endpoint para validar um cartão",
    )
    def post(self, request):
        card_number = request.data.get('card_number')
        if card_number:
            card = Card.objects.filter(hash_id=hashlib.sha256(card_number.encode()).hexdigest()).first()
            if card:
                serializer = CardSerializer(card)
                return Response(serializer.data['uuid'], status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Card not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)