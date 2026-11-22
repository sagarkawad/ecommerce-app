from django.urls import path
from . import views

urlpatterns = [
    path("", views.products),
    path("health/", views.health_check),
    path("<int:product_id>/", views.product_details)
]