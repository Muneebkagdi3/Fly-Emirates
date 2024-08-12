from django.urls import path
from . import views



urlpatterns = [
    path("search/", views.search, name= "search"),
    path("category/<int:pk>",views.CategoryDetailView.as_view(),name="category"),
    path("payment/<int:planeId>", views.payment, name="payment"),
    path("book/<str:TicketNo>", views.book, name="book")
]
