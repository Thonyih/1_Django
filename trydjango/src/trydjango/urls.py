"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from products.views import homepage_view, contact_view, about
from products.views import hometest, basehtml
from products.views import product_create_view
from products.views import product_detailhtml, product_detail_view, product_delete_view, product_list_view




# FWY - I CREATED A NEW URL FILE DIRECTLY IN THE products FOLDER
# I SHOULD GO THERE TO SEE WHAT WAS WORKING HERE
urlpatterns = [ 

    path('productlist/', include('products.urls')), #Incluir imports novos que criei  

    path('', homepage_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls, name='admin2'),
    path('about/', about, name='about'),
    path('hometest/', hometest, name='hometest'),
    path('base/', basehtml, name='basehtml'),
    
 
    path('productCreate/', product_create_view, name='productCreate'),  
    path('detail/', product_detailhtml, name="detail"),

]

