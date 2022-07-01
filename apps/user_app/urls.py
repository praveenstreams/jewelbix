
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# usermangerouter= DefaultRouter()
# usermangerouter.register('user-manage', UserManageView, basename= 'user-manage')

urlpatterns = [
    path('user-create', UserManageView.as_view()),
    path('login', UserLoginView.as_view())

]