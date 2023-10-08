from django.urls import path
from .views import *

# The paths for dash
urlpatterns = [
    path('error-codes/', ErrorCodeList.as_view(), name='error-code-list'),
    path('products/', ProductList.as_view(), name='products'),
    # path('login', views.UserLogin.as_view(), name='login'),
    # path('logout', views.UserLogout.as_view(), name='logout'),
    # path('dash', views.UserView.as_view(), name='user')
]
