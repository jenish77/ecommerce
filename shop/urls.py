from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="AboutUs"),
    path('Contact/',views.Contacts,name="ContactUs"),
    path('tracker/',views.tracker,name="Tracking"),
    path('search/',views.search,name="search"),
    path('productive/<int:myid>',views.productive,name="product"),
    path('checkout/',views.checkout,name="Checkout"),

]