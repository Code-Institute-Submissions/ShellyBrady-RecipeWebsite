from . import views
from django.urls import path
from .views import Submission, Recipe

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/', views.RecipeList.as_view, name='recipe'),
    path('submit/', views.Submission, name='submit'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
