from django.urls import path, include
from .views import *

app_name = 'shop'
urlpatterns = [
    path('orders/', include('orders.urls', namespace='orders')),
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list,
        name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]