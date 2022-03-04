from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_view, name="list_view"),
    path('chat/', views.chat_index, name="chat_index"),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('<id>/details/', views.detail_view, name="detail_view"),
    path('<id>/update/', views.update_view, name="update_view"),
    path('<id>/delete/', views.delete_view, name="delete_view"),
    path('<id>/', views.buy_view, name="buy_view"),
]