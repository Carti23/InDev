from django.urls import path
from .views import RegisterView, MyObtainTokenPairView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyObtainTokenPairView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]