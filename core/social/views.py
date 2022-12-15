from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls.base import reverse_lazy
from .models import SocialComment, SocialPost
# Create your views here.


class PostEditview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model=SocialPost
    fields=['body']
    template_name= 'pages/social/edit.html'

    def get_success_url(self):
        pk= self.get_object()
        return reverse_lazy('social:post-detail', kwargs={'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author