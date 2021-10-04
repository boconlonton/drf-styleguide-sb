from django.urls import path

from styleguide_example.users.v1.apis import UserListApi
from styleguide_example.users.v1.apis import UserCreateApi
from styleguide_example.users.v1.apis import UserDetailApi

app_name = 'users'

urlpatterns = [
    path('', UserListApi.as_view(), name='list'),
    path('<int:user_id>', UserDetailApi.as_view(), name='detail'),
    path('create/', UserCreateApi.as_view(), name='create'),
]
