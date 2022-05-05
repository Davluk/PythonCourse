from django.urls import include, path  
from simple_webapp import views

urlpatterns=[
    path("", views.Home.as_view() ),
    path("generic/", views.Generic.as_view() ),
    path("elements/", views.Elements.as_view() )
]