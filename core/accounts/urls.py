from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path("<username>/", views.UserProfileView.as_view(), name='profile'),
    path("edit/", views.UserProfileEdit.as_view(), name='edit-profile'),
]