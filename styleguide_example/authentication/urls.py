from django.urls import path

from styleguide_example.authentication.apis import TokenObtainPairView
from styleguide_example.authentication.apis import TokenRefreshView

app_name = 'authentication'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),
         name='get-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='refresh-token'),
]
