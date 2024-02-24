from django.urls import path
from .  import views 

urlpatterns = [
    path("", views.index, name= "Taxes"),
    path("<int:number>", views.taxCalc, name= "Calculate the tax"),
    path("taxrate", views.taxrate, name= "Tax Rate")
]