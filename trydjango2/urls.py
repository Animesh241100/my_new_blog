"""trydjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

#from pages import views , instead of this do the below thing, its much better.
from pages.views import home_view, file1_view, present_view  #wow, we imported the actual function itself

#from Product_app.views import (
       # product_detail_view,
   #     product_create_view,
     #   dynamic_lookup_view,
     #   product_delete_view,
      #  product_list_view,
    


urlpatterns = [
    path('', home_view),
    #path('admin/', admin.site.urls),
    #path('fire/', views.home_view), instead of this do the below thing, its much better.
    #path('fire/', file1_view ),
    #path('present/', present_view), #cool
   # path('product/', include('Product_app.urls')),

    path('blogs/', include('Blog.urls')),


    #path('product/', product_detail_view), #getting started with database stuff
    #path('product/<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    #path('product/create/', product_create_view, name='product-create'),
    #path('product/delete/<int:my_id>/', product_delete_view, name='product-delete'),
    #path('product/productlist/', product_list_view) 
]
