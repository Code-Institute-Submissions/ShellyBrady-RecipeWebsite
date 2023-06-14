from . import views
from django.urls import path
from .views import Submission, Recipe, RecipeLike

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('members', views.MembersRecipesList.as_view(), name='members'),
    path('submit/', views.Submission, name='submit'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
