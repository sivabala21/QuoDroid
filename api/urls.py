from django.urls import path
from .views import TestView

urlpatterns = [
    path('tests/api',TestView.as_view(),name="tests")
]
