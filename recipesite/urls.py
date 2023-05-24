from . import views
from django.urls import path
from .views import Submission, approved_recipes

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('approved-recipes/', approved_recipes, name='approved_recipes'),
    path('submit/', views.Submission, name='submit'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
