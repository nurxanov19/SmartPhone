from django.urls import path
from .views import home, phone_list, phone_detail, create_phone, create_phone2, update_phone, delete_phone

urlpatterns = [
    path('', home, name='home'),
    path('phone-list/', phone_list, name='phone-list'),
    path('phone/<int:pk>', phone_detail, name='phone-detail'),
    path('create-phone/', create_phone, name='create-phone'),
    path('create-phone/', create_phone2, name='create-phone2'),
    path('update-phone/<int:pk>/', update_phone, name='update-phone'),
    path('delete-phone/<int:pk>/', delete_phone, name='delete-phone')
]