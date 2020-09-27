from django.urls import path
from .views import(
    home,
    encrypt,
    decrypt,
    encrypted,
    decrypted
)

urlpatterns = [
    path('encryption/', home, name='encryption'),
    path('encrypt/', encrypt, name='encrypt'),
    path('decrypt/', decrypt, name='decrypt'),
    path('encrypted/', encrypted, name='encrypted'),
    path('decrypted/', decrypted, name='decrypted'),   
]
