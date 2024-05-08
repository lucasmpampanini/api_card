from user_authenticate import views
from django.urls import path

urlpatterns = [
    path('create', views.CreateUserView.as_view()),
]
