from django.urls import path, include

from rest_framework.routers import DefaultRouter

from origindb import views

router = DefaultRouter()

app_name = 'origindb'

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoriesAPIView.as_view(), name='categories'),
    path('products/', views.ProductsAPIView.as_view(), name='products'),
    path('components/', views.ComponentsAPIView.as_view(), name='components'),
    # path('components-detail/', views.ComponentsDetailAPIView.as_view(), name='components-detail'),
    ]
