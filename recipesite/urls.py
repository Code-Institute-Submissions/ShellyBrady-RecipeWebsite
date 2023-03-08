from . import views
from django.urls import path
from .views import submit_recipe

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('member_recipes/', views.member_recipes, name='member_recipes'),
    path('submit/', views.submit_recipe, name='submit'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
