from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health_check),
    path("products/", views.products),
    path("products/<int:product_id>/", views.product_details)
]