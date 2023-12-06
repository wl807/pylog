from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list , name="post_list"),
    # <> 으로 동적으로 값을 받고, 해당하는 view 의 인수로 전달
    path('<int:post_id>/', views.post_detail, name="post_detail" ), 
    path('add/', views.post_add, name="post_add" ), 
]
