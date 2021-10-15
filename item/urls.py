from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CuserPostListView,
    PostBidView,
    PostBidAcceptView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'item-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('cuser/', CuserPostListView.as_view(), name='cuser-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/bid/', PostBidView.as_view(), name = 'post-bid'),
    path('post/<int:pk>/bid/accept/', PostBidAcceptView.as_view(), name = 'post-bid-accept'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
]