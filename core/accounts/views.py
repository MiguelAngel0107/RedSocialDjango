from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from accounts.models import Profile
# Create your views here.

User = get_user_model()

class UserProfileView(View):


    def get(self, request, username, *args, **kwargs):
        user=get_object_or_404(User, username=username)    
        profile = Profile.objects.get(user=user)
        context={
            'user': user,
            'profile': profile,

        }
        return render(request, 'users/detail.html', context)


class UserProfileEdit(View):

    def get(self, request):


        return render(request, '<h1>Hola</h1>')