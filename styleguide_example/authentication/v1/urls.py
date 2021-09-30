from django.urls import path

from styleguide_example.authentication.v1.apis import CustomTokenObtainPairView
from styleguide_example.authentication.v1.apis import CustomTokenRefreshView

app_name = 'authentication'

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(),
         name='get-token'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(),
         name='refresh-token'),
]
