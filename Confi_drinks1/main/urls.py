from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name = "home"),
    path("cm",views.cm, name = "cm"),
    path("search_of_ingrid",views.search_of_ingrid, name = "search_of_ingrid"),
    path("prof",views.prof, name = "prof"),
    path("coctail_info",views.coctail_info, name = "coctail_info"),
]