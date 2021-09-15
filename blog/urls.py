
from django.urls import path
from django.conf.urls import url
from blog.views import (
	create_blog_view,
	detail_blog_view,
	edit_blog_view,
	LikeView,
	delete_post,
	comment,
	
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
    path('<int:pk>/like_post/', LikeView, name="like_post"),
    path('delete/<slug>',delete_post,name='delete'),
   path('<slug>/comment', comment, name="comment")
 ]
