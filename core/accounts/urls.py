from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    #path("test/", views.test, name='test'),
    path("<username>/", views.UserProfileView.as_view(), name='profile'),
    path("<username>/edit/", views.EditProfile, name='edit-profile'),
]