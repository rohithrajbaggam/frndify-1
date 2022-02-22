from django.urls import path 
from . import views 
from .views import (PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView,
                    PostListView, PostDeleteView ) 
urlpatterns = [ 
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('userprofiledata', views.userprofilelist, name='user-profile-list'),
    # page urls

    path('pages/', PageListView.as_view(), name='page-list'),
    path("page/<int:pk>/", PageDetailView.as_view(), name='page-detail'),
    path('page/new', PageCreateView.as_view(), name='page-create'),
    path("page/<int:pk>/update/", PageUpdateView.as_view(), name='page-update'),
    path("page/<int:pk>/delete/", PageDeleteView.as_view(), name='page-delete'),
    path("page/profile/<int:pk>/<page_title>/", views.page_profile, name='page-profile'),
    # page post utls
    path("page/<int:pk>/create-post/", views.PostCreateView, name='post-create'),
    path("posts/", views.postlistview, name='post-list'),
    path("post/<int:pk>/", views.postdetailview, name='post-detail'),
    path("post/<int:pk>/update/", views.PostUpdateView, name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    # save and unsave
    path('saved-posts/', views.savedPostList, name='saved-posts'),
    path('Save/<pk>/', views.save_post, name='save' ),
    path('Unsave/<pk>/', views.unsave_post, name='unsave'),

]