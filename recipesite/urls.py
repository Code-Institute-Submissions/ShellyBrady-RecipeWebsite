from . import views
from django.urls import path
from .views import (RecipeList, RecipeDetail, RecipeLike, SubmissionDetail,
                    SubmissionListView, SubmissionLike, EditProfile,
                    EditSubmission, DeleteSubmission)

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('submission_list', views.SubmissionListView.as_view(),
         name='submission_list'),
    path('submission_detail/<slug:slug>', views.SubmissionDetail.as_view(),
         name='submission_detail'),
    path('edit_submission/<int:submission_id>/', EditSubmission.as_view(),
         name='edit_submission'),
    path('delete_submission/<int:submission_id>/',
         views.DeleteSubmission.as_view(),
         name='delete_submission'),
    path('submit/', views.create_submission, name='submit'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('submission_like/<slug:slug>', views.SubmissionLike.as_view(),
         name='submission_like'),
]
