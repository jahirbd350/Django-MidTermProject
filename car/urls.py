from django.urls import path
from . import views
urlpatterns = [
    path('add-car-brand/', views.addCarBrandCreateView.as_view(),
         name='add-car-brand'),
    path('add-car-details/', views.addCarDetailsCreateView.as_view(),
         name='add-car-details'),
    path('car-details/<int:id>/', views.carDetailsView.as_view(), name='car-details'),


    path('place-order/<int:id>/', views.placeOrder, name='place-order'),
]
