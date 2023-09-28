from django.urls import path
from.views import OrdersListView, create_order, OrderDetailView


app_name = 'orders'
urlpatterns = [
    path('', OrdersListView.as_view(), name='order-list'),
    path('new_order/', create_order, name='create_order'),
   

]
