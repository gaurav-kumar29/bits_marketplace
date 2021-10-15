from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import(
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
) 
from .models import Post

#def home(request):
 #   context = {
  #      'posts': Post.objects.all()
   # }
    #return render(request, 'item/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'item/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'item/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(seller=user).order_by('-date_posted')


class CuserPostListView(ListView):
    model = Post
    template_name = 'item/cuser_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'desc', 'base_price', 'item_image']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'desc', 'base_price', 'item_image']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False

class PostBidView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['bid', 'bid_phone']
    template_name = 'item/post_bid.html'

    def form_valid(self, form):
        post = self.get_object()
        if form.cleaned_data['bid'] < post.base_price:
            form.add_error('bid', 'Bid cannot be less than the base price')
            return self.form_invalid(form)
        if form.cleaned_data['bid'] <= post.bid:
            form.add_error('bid', 'Current Bid cannot be less than the Highest Bid')
            return self.form_invalid(form)
        return super(PostBidView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user != post.seller:
            return True
        return False

class PostBidAcceptView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = []
    template_name = 'item/post_bid_accept.html'

    def form_valid(self, form):
        form.instance.status = 'Sold'
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False
