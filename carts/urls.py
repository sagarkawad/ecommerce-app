from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart),
    path("add-item/", views.add_items_to_cart)
]