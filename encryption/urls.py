from django.urls import path
from .views import encrypt_text, decrypt_text

urlpatterns = [
    path('encrypt/', encrypt_text, name='encrypt'),
    path('decrypt/', decrypt_text, name='decrypt'),
]
