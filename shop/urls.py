from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='Home'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='Contact Us'),
    path('search/',views.search,name='Search'),
    path('productView/',views.productView,name='product view')
]
