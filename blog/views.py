from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model= Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

class UserPostListView(ListView):
    model= Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')    

class PostDetailView(DetailView):
    model= Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model= Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
            post=self.get_object()
            if self.request.user==post.author:
                return True
            return False

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model= Post
    success_url='/'
    def test_func(self):
            post=self.get_object()
            if self.request.user==post.author:
                return True
            return False

'''@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})'''

class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']
    success_url='/'
    def form_valid(self, form):
        _forum = get_object_or_404(Post, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.post = _forum
        return super().form_valid(form)

def comment_posted( request ):
    referer = request.META.get('HTTP_REFERER', None)
    return HttpResponseRedirect(referer)
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})