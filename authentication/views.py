# coding=utf-8

from django.contrib.auth.models import User
from rest_framework.views import APIView

from api.extensions.response import HttpResponse


class Register(APIView):
    """
        API View to handle register
    """
    http_method_names = ['post']

    def post(self, request, format=None):
        data = request.data
        password = data.get('password')
        user = User.objects.create(**data)
        user.set_password(password)

        return HttpResponse(message='Success')
