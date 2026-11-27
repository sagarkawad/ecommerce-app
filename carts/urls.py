from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart),
    path("add-item/", views.add_items_to_cart),
    path("remove-item/", views.remove_items_from_cart),
    path("update-product-quantity/", views.add_or_substract_item_quantity),
    path("subtotal/", views.calculate_subtotal)
]