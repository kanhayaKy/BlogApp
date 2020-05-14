from django.urls import path
from .views import home,post,create,update,delete

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('post/<int:pk>',post.as_view(),name="post-details"),
    path('post/new/',create.as_view(),name="create-post"),
    path('post/update/<int:pk>/',update.as_view(),name="update-post"),
    path('post/<int:pk>/delete/',delete.as_view(),name="delete-post")
]
