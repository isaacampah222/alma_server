from django.urls import path
from knox import views as knox_views
from .views import SingleOrderView,RegisterAPI,LoginAPI

urlpatterns = [
    path('order/',SingleOrderView.as_view()),
    path('order/<int:id>/', SingleOrderView.as_view()),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('logout/',knox_views.LogoutView.as_view()),
]