from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.categoryList, name="categories"),
    path('new', views.categoryAddNew, name="categories.add"),
    path('<int:cid>', views.categoryDetails, name='categories.details'),
    path('delete/<int:cid>', views.categoryDelete, name='categories.delete'),
    path('update/<int:cid>', views.categoryUpdate, name='categories.update'),
]