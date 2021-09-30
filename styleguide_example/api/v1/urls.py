from django.urls import path
from django.urls import include

from django.urls import re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'api-v1'

schema_view = get_schema_view(
    openapi.Info(
        title="GoPMS APIs Documentation",
        default_version='v1',
        description="This is a description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_pattern = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]

urlpatterns = [
    path('authentication/',
         include('styleguide_example.authentication.v1.urls')),
    path('users/',
         include('styleguide_example.users.v1.urls')),
    *swagger_pattern
]
