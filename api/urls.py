from django.urls import path
from .views import TestView

urlpatterns = [
    path('testai/tests/v1/execute',TestView.as_view(),name="tests")
]
