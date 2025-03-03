from django.urls import path
from .views import home, phone_list, phone_detail, create_phone, create_phone2, update_phone, delete_phone, \
    phone_create_from, contact_form, update_phone_form

urlpatterns = [
    path('', home, name='home'),
    path('phone-list/', phone_list, name='phone-list'),
    path('phone/<int:pk>', phone_detail, name='phone-detail'),
    path('create-phone/', create_phone, name='create-phone'),
    path('create-phone/', create_phone2, name='create-phone2'),
    #path('update-phone/<int:pk>/', update_phone, name='update-phone'),
    path('delete-phone/<int:pk>/', delete_phone, name='delete-phone'),
    path('phone-form/', phone_create_from, name='phone-form'),
    path('contact-form/', contact_form, name='contact-form'),
    path('phone-update/<int:pk>/', update_phone_form, name='update-phone-form'),

]