from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('products',views.products,name="products"),
    path('contact',views.contact,name="contact"),
    path('orders',views.orders,name="orders"),
    path('checkout/',views.checkout,name="checkout"),
    path('handlerequest/',views.handlerequest,name="handlerequest"),
]