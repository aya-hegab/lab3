from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.productList, name="products"),
    path('new', views.productAddNew, name="products.add"),
    path('newform', views.productAddNewForm, name="products.addform"),
    path('<int:pid>', views.productDetails, name='products.details'),
    path('delete/<int:pid>', views.productDelete, name='products.delete'),
    path('update/<int:pid>', views.productUpdate, name='products.update'),
    
]
