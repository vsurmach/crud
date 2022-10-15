from django.urls import path

from .views import get_one, view_cars, new_car, edit_car, delete_car, model_new_car, model_view_cars, model_edit_car, \
model_delete_car, form_new_car, form_edit_car, form_view_cars, form_delete_car


app_name = 'crud'

urlpatterns = [
    path('', get_one),
    path('cars/', view_cars, name='view_cars'),
    path('new_car/', new_car, name='new_car'),
    path('edit_car/<int:pk>/', edit_car, name='edit_car'),
    path('delete_car/<int:pk>/', delete_car, name='delete_car'),

    path('model_new/', model_new_car, name='model_new'),
    path('model_view/', model_view_cars, name='model_view'),
    path('model_edit/<int:pk>/', model_edit_car, name='model_edit'),
    path('model_delete/<int:pk>/', model_delete_car, name='model_delete'),

    path('form_new/', form_new_car, name='form_new'),
    path('form_view/', form_view_cars, name='form_view'),
    path('form_edit/<int:pk>/', form_edit_car, name='form_edit'),
    path('form_delete/<int:pk>/', form_delete_car, name='form_delete'),
]