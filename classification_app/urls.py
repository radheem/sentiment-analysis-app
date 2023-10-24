from django.urls import path
from .views import history, classification,delete_record

urlpatterns = [
    path('classify/',classification, name='classify'),
    path('history/',history, name='history'),
    path('delete/<int:id>', delete_record, name='delete_record'),
]