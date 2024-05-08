from card.views import CardView, CardValidationView
from django.urls import path


urlpatterns = [
    path('insert', CardView.as_view()),
    path('validate', CardValidationView.as_view()),
]