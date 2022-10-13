from django.urls import path
from .views import *

urlpatterns = [
    path('create-poster-by-admin/', PosterView.as_view(), name="create-poster-by-admin"),
    path('update-poster-by-admin/', PosterView.as_view(), name="update-poster-by-admin"),
    path('get-poster-by-admin/', PosterView.as_view(), name="get-poster-by-admin"),
    path('get-poster-by-admin/<int:pk>/', PosterView.as_view(), name="get-poster-by-admin"),
    path('delete-poster-by-admin/<int:pk>/', PosterView.as_view(), name="delete-poster-by-admin"),

]