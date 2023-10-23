from django.urls import path, include, re_path
from .views import history, classification

urlpatterns = [
    path('classify/',classification, name='classify'),
    path('history/',history, name='history'),
]