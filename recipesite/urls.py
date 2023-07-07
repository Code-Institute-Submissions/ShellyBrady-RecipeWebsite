from . import views
from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeLike, SubmissionDetail, SubmissionListView, SubmissionLike

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('submission_list', views.SubmissionListView.as_view(), name='submission_list'),
    path('submission_detail/<str:pk>', views.SubmissionDetail.as_view(), name='submission_detail'),
    path('submit/', views.create_submission,  name='submit'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('submission_like/<slug:slug>', views.SubmissionLike.as_view(), name='submission_like'),

]
