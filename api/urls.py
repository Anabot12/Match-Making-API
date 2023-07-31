from api.views import ListAPI
from django.urls import path

urlpatterns = [
path('', ListAPI.as_view()),
]