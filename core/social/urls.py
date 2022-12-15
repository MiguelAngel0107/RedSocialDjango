from django.urls import path
from .views import PostEditview

app_name='social'

urlpatterns = [
    path("edit/", PostEditview.as_view(), name="edit-post")
]
