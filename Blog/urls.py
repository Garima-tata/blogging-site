from django.urls import path
from .views import BlogListView, post, about, category, createe, signin, signup, logout_view, delete_post

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout_view, name='logout'),
    
    path("", BlogListView, name='home'),
    path("blog/<slug:url>/", post),
    path("blogCategories/<slug:url>/", category),
    path("about/", about),
    path("create/", createe),
    
    
    path('blog/<int:post_id>/delete/', delete_post, name='delete_post'),

    # path("tinymce/", include("tinymce.urls")),
]


