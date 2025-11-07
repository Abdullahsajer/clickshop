from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('products/', views.products_view, name='products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
