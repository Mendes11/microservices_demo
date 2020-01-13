from django.urls import path

from apps.api import views

app_name = 'v1'


urlpatterns = [
    path('product-types/', views.ProductTypeListCreateView.as_view(),
         name='product_type_list'),
    path('products/', views.ProductListCreateView.as_view(),
         name='product_list'),
]
