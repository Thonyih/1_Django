
from django.contrib import admin
from django.urls import path

from .views import (homepage_view, contact_view, about, hometest,
                    basehtml, product_create_view, product_detailhtml,
                    product_detail_view, product_delete_view,
                    product_list_view,)


urlpatterns = [

    path('', product_list_view, name='productlist'),

    path('productdetail/<int:my_id>/', product_detail_view, name='productDetail'),

    path('productdelete/<int:my_id>/',  product_delete_view, name='productdelete'),

]