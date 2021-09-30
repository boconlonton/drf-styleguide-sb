from django.urls import path

from styleguide_example.users.v1.apis import UserListApi
from styleguide_example.users.v1.apis import UserCreateApi

app_name = 'users'

urlpatterns = [
    path('', UserListApi.as_view(), name='list-user'),
    path('create/', UserCreateApi.as_view(), name='create-user')
]
