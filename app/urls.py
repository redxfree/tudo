from django.urls import path,include
from .views import *


urlpatterns = [
    path('',CommodityCreate.as_view(),name='home'),
    path('list',CommodityList.as_view(),name='list'),
    path('update/<int:pk>',CommodityUpdate.as_view(),name='update'),
    path('destroy/<int:pk>',CommodityDestroy.as_view(),name='destroy'),
    path('active',Active.as_view(),name='active'),
]
