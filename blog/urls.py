from django.urls import path
from .views import  (
            PostListView,
            PostDetailView,
            PostCreateView,
            PostUpdateView,
            PostDeleteView,
            UserPostListView
            )
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('resume/', views.resume, name='blog-resume'),
    path('gallery/', views.gallery, name='blog-gallery'),
    path('delete/<int:image_id>/', views.delete_image, name='delete-image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit-image'),





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
