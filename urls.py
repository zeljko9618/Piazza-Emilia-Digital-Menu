from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name="home"),
    path('meal_description', views.MenuItemDetail.as_view(), name="meal_description")
]
