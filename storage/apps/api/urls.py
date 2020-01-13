from django.urls import path
from apps.api import views

app_name = 'v1'


urlpatterns = [
    path('storages/', views.StorageListView.as_view(),
         name='storage_list'),
    path('storages/<uuid:pk>/', views.StorageDetailView.as_view(),
         name='storage_detail'),
    path('storage-operations/', views.StorageOperationListCreateView.as_view(),
         name='storage_operation_list'),
]
