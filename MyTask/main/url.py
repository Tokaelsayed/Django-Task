from django.urls import path
from . import views

urlpatterns=[
 
   
    path("", views.Barcharts,name="Barcharts"),
    path("secondbarchart/", views.SecondBarcharts,name="SecondBarcharts"),
    path("thirdbarchart/", views.ThirdBarcharts,name="ThirdBarcharts"),
    path("fourthbarchart/", views.FourthBarcharts,name="ThirdBarcharts"),
    path("dategraph/", views.Dategraph,name="ThirdBarcharts"),
    path("seconddategraph/", views.SecondDategraph,name="ThirdBarcharts"),
    path("thirddategraph/", views.ThirdDategraph,name="ThirdBarcharts"),

]