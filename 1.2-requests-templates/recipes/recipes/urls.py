from django.urls import path
from calculator.views import home, recipes

urlpatterns = [
    path('', home, name='home'),
    path('<str:recipe>/', recipes)
]
