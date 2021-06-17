from django.urls import path
from .views import sub_list

urlpatterns = [
    path('sub/', sub_list),
]
