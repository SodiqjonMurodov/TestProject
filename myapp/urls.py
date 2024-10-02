from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='products'),
    path('<int:pk>', views.ProductListAPIView.as_view(), name='products'),
]
