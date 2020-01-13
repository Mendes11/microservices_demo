from django.urls import path
from apps.api import views


app_name = 'v1'


urlpatterns = [
    path('orders/', views.ProductOrderListCreateView.as_view(),
         name='product_order_list'),
    path('orders/<uuid:pk>/', views.ProductOrderDetailView.as_view(),
         name='product_order_detail'),
]
