from django.urls import path
from . import views

urlpatterns = [
    path("produk/", views.product_list, name="product_list"),
    path(
        "produk/<slug:slug>/",
        views.product_detail,
        name="product_detail"
    ),
]