from django.urls import path

from .views import ItemsView


app_name = "articles"

urlpatterns = [
    path('items/', ItemsView.as_view()),
    path('items/<int:pk>', ItemsView.as_view()),
]