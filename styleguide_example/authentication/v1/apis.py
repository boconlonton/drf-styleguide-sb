from rest_framework.status import HTTP_200_OK

from rest_framework.serializers import Serializer
from rest_framework.serializers import CharField

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi


class CustomTokenObtainPairView(TokenObtainPairView):
    """This API is used for retrieving access token for a validated user
    Params:
        - email (str): specify user email for validating
        - password (str): specify user password for validating
    """

    class InputToken(Serializer):

        email = CharField(min_length=5, max_length=12, required=False)
        password = CharField()

    class OutputToken(Serializer):
        """Docstring for response output"""

        access = CharField(min_length=5)
        refresh = CharField()

        def create(self, validated_data):
            raise NotImplementedError()

        def update(self, instance, validated_data):
            raise NotImplementedError()

    @swagger_auto_schema(
        operation_id='Get token API',
        request_body=InputToken,
        responses={HTTP_200_OK: openapi.Response('Token', OutputToken)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """This API is used for refreshing token"""

    class OutputRefreshToken(Serializer):
        access = CharField()

        def create(self, validated_data):
            raise NotImplementedError()

        def update(self, instance, validated_data):
            raise NotImplementedError()

    @swagger_auto_schema(
        responses={
            HTTP_200_OK: openapi.Response('Refresh Token', OutputRefreshToken)
        })
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
