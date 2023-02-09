from django.shortcuts import render
from rest_framework.views import APIView
from applications.account.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Вы успешно зарегистрировались. Вам отправлено письмо с активацией", status=201)


User = get_user_model()

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code - ''
            user.save()
            return Response("Успешно", status=200)
        except User.DoesNotExist:
            return Response("Link expired", status=400)

class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutAPIView(APIView):
    def post(self, request):
        try:
            user = request.user
            token = Token.objects.get(user=user).delete()
            return Response("Вы успешно разлогинились!!!", status=200)
        except:
            return Response(status=403)