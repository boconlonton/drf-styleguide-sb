from rest_framework.status import HTTP_200_OK

from rest_framework.serializers import Serializer
from rest_framework.serializers import CharField

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from drf_yasg.utils import swagger_auto_schema


class TokenObtainPairView(TokenObtainPairView):
    """This API is used for retrieving access token for a validated user
    Params:
        - email (str): specify user email for validating
        - password (str): specify user password for validating
    """

    class OutputToken(Serializer):
        """Docstring for response output"""

        access = CharField(min_length=5)
        refresh = CharField()

        def create(self, validated_data):
            raise NotImplementedError()

        def update(self, instance, validated_data):
            raise NotImplementedError()

    @swagger_auto_schema(responses={HTTP_200_OK: OutputToken})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshView(TokenRefreshView):
    class OutputRefreshToken(Serializer):
        access = CharField()

        def create(self, validated_data):
            raise NotImplementedError()

        def update(self, instance, validated_data):
            raise NotImplementedError()

    @swagger_auto_schema(responses={HTTP_200_OK: OutputRefreshToken})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
