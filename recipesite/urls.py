from . import views
from django.urls import path
from .views import Submission, Post, MemberRecipe

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('submit/', views.Submission, name='submit'),
    path('memberrecipe/', views.MemberRecipeList.as_view(), name='memberrecipe'),
    path('<slug:slug>/', views.MemberRecipeDetail.as_view(), name='member_recipe_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
