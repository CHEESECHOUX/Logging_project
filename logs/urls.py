from django.urls import path
from logs.views import LogView

urlpatterns = [
    path('/log', LogView.as_view())
]
