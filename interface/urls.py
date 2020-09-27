from django.urls import path
from interface import views
from interface.views import (
    ArsenalView,
    VehiclesView,
    ArsenalMoreInfo,
    VehicleMoreInfo,
    
)
from encryption.views import(
    home,
    encrypt,
    decrypt,
    encrypted,
    decrypted
)


urlpatterns = [
    path('', views.cover, name='cover'),
    path('contact', views.contact, name='contact'),
    path('categories', views.categories, name='categories'),
    path('check', views.check, name='check'),
    path('arsenal', ArsenalView.as_view(), name='arsenal'),
    path('vehicles', VehiclesView.as_view(), name='vehicles'),
    path('arsenal/<int:pk>/', ArsenalMoreInfo.as_view(), name='more-info'),
    path('vehicles/<int:pk>/', VehicleMoreInfo.as_view(), name='more-info-vehicles'),
    path('help', views.help, name='help'),
    path('encryption/', home, name='encryption'),
    path('encrypt/', encrypt, name='encrypt'),
    path('decrypt/', decrypt, name='decrypt'),
    path('encrypted/', encrypted, name='encrypted'),
    path('decrypted/', decrypted, name='decrypted'), 
]