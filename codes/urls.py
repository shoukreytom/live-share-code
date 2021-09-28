from django.urls import path

from codes import views


urlpatterns = [
    path("file/list/", views.FileListAPIView.as_view()),
    path("file/list/shared/", views.SharedFileListAPIView.as_view()),
    path("file/<int:pk>/get/", views.FileRetrieveAPIView.as_view() ),
    path("file/<int:pk>/edit/", views.edit_file ),
    path("file/<int:pk>/delete/", views.delete_file ),
    path("file/<int:pk>/share/", views.share_file ),
]

