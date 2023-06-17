from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, Http404, HttpResponse
from recipesite.models import Recipe, Submission, Comment
from .forms import CommentForm, SubmissionForm
from django.contrib import messages
from django.views.generic import DetailView


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


def get_recipe(request):

    queryset = Recipe.objects.filter(status=1)

    return render(request, 'index.html', {'queryset': queryset})


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        pk = self.kwargs.get('pk')
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        content_type = ContentType.objects.get_for_model(recipe)
        comments = Recipe.objects.filter(is_approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class SubmissionListView(generic.ListView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission_list.html'
    context_object_name = 'submission_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submissions'] = Submission.objects.all()
        return context


def get_submission(request):

    queryset = Submission.objects.filter(status=1)

    return render(request, 'index.html', {'queryset': queryset})


def create_submission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            Submission = form.save(commit=False)
            Submission.user = request.user
            Submission.save()
            messages.success(request, 'Your recipe has been submitted successfully and is awaiting approval by the admin.')
        return redirect('submission_list', slug=submission.slug)
    else:
        form = SubmissionForm()

    return render(request, 'submission.html', {'form': form})


class SubmissionDetail(View):

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs.get('pk')
        queryset = Submission.objects.filter(status=1)
        submission = get_object_or_404(queryset, pk=pk)
        content_type = ContentType.objects.get_for_model(Submission)
        comments = Submission.objects.filter(is_approved=True).order_by("-created_on")
        liked = False
        if submission.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "submission_detail.html",
            {
                "submission": submission,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = Submission.objects.filter(status=1)
        submission = get_object_or_404(queryset, pk=pk)
        comments = submission.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if submission.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "submission_detail.html",
            {
                "submission": submission,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class SubmissionLike(View):

    def post(self, request, slug, *args, **kwargs):
        submission = get_object_or_404(Recipe, slug=slug)
        if submission.likes.filter(id=request.user.id).exists():
            submission.likes.remove(request.user)
        else:
            submission.likes.add(request.user)

        return HttpResponseRedirect(reverse('submission_detail', args=[slug]))
