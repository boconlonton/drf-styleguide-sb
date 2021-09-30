from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi

from styleguide_example.api.mixins import ApiErrorsMixin
from styleguide_example.api.pagination import get_paginated_response
from styleguide_example.api.pagination import DefaultLimitOffsetPagination

from styleguide_example.users.v1.selectors import user_list
from styleguide_example.users.models import BaseUser


class UserListApi(ApiErrorsMixin, APIView):
    """List all users API

    FilterParams:
        - id (int): specify the user id to be filtered
        - email (str): specify the user email to be filtered
        - is_admin (bool) specify the admin flag to be filtered

    """
    class Pagination(DefaultLimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        # Important: If we use BooleanField, it will default to False
        is_admin = serializers.NullBooleanField(required=False)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaseUser
            fields = (
                'id',
                'email',
                'is_admin'
            )

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response('User List',
                                                 OutputSerializer(many=True))
        })
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self
        )


class UserCreateApi(ApiErrorsMixin, APIView):
    """Create user API"""

    class InputUserSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        # Important: If we use BooleanField, it will default to False
        is_admin = serializers.NullBooleanField(required=False)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaseUser
            fields = (
                'id',
                'email',
                'is_admin'
            )

    @swagger_auto_schema(responses={200: OutputSerializer(many=True)})
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self
        )
