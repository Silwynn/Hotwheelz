from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('car_brands/', views.car_brand_list, name='car_brand_list'),
    path('car_brands/<int:pk>/', views.car_brand_detail, name='car_brand_detail'),
    path('car_brands/create/', views.car_brand_create, name='car_brand_create'),
    path('car_brands/<int:pk>/update/', views.car_brand_update, name='car_brand_update'),
    path('car_brands/<int:pk>/delete/', views.car_brand_delete, name='car_brand_delete'),
    path('car_brands/<int:brand_id>/car_models/<int:model_id>/', views.car_model_detail, name='car_model_detail'),
    path('car_brands/<int:brand_id>/car_models/create/', views.car_model_create, name='car_model_create'),
    path('car_brands/<int:brand_id>/car_models/<int:model_id>/update/', views.car_model_update, name='car_model_update'),
    path('car_brands/<int:brand_id>/car_models/<int:model_id>/delete/', views.car_model_delete, name='car_model_delete'),
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('collections/create/', views.collection_create, name='collection_create'),
    path('collections/<int:collection_id>/update/', views.collection_update, name='collection_update'),
    path('collections/<int:collection_id>/delete/', views.collection_delete, name='collection_delete'),
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/create/', views.owner_create, name='owner_create'),
    path('owners/<int:owner_id>/update/', views.owner_update, name='owner_update'),
    path('owners/<int:owner_id>/delete/', views.owner_delete, name='owner_delete'),
]
