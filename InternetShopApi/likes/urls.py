from django.urls import path
from . import views
urlpatterns = [
    path('likes/', views.LikesView.as_view())
]
