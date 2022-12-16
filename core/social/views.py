from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls.base import reverse_lazy
from django.views.generic import View


from .models import SocialComment, SocialPost

# Create your views here.

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)
        #form = SocialCommentForm()

        #comments = SocialComment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
        #    'form': form,
        #    'comments':comments
        }

        return render(request, 'pages/social/detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)

        #form = SocialCommentForm(request.POST)

        #if form.is_valid():
        #    new_comment = form.save(commit=False)
        #    new_comment.author = request.user
        #    new_comment.post = post
        #    new_comment.save()

        #comments = SocialComment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            #'form': form,
        #    'comments':comments
        }

        return render(request, 'pages/social/detail.html', context)


class PostEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model=SocialPost
    fields=['body']
    template_name= 'pages/social/edit.html'

    def get_success_url(self):
        pk= self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=SocialPost
    template_name='pages/social/delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author