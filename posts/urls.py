from django.urls import path
from .views import post_list ,singel_post,new_post,edit_post,delete_post

app_name='posts'

urlpatterns = [
    path('',post_list,name='post_list'),
    path('<int:id>',singel_post,name='post_detail'),
    path('new',new_post,name='new_post'),
    path('<int:id>/edit',edit_post,name='edit_post'),
    path('<int:id>/delete',delete_post,name='delete_post'),
]
