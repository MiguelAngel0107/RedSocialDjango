
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class HomeView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)