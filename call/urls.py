from django.urls import path
from . import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
    path("call/<str:room_name>/", views.join_room, name="join-room"),

]
