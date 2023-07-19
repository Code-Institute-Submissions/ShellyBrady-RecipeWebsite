from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, Http404, HttpResponse
from recipesite.models import Recipe, Submission, Comment
from .forms import CommentForm, SubmissionForm
from django.contrib import messages
from django.views.generic import DetailView
from django.utils.text import slugify


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


def get_recipe(request):

    queryset = Recipe.objects.filter(status=1)

    return render(request, 'index.html', {'queryset': queryset})


class RecipeDetail(View):
    model = Recipe
    template_name = 'recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['comments'] = recipe.comments.all()
        return context

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        title = request.GET.get('title')
        content_type = ContentType.objects.get_for_model(recipe)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
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
        title = request.GET.get('title')
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

    def get_queryset(self):
        return Submission.objects.filter(status=1)


def create_submission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.username_id = request.user
            submission.slug = slugify(submission.title)
            submission.save()
            messages.success(request, 'Your recipe has been submitted successfully and is awaiting approval by the admin.')
        return redirect('submission_list')
    else:
        form = SubmissionForm()

    return render(request, 'submission.html', {'form': form})


class SubmissionDetail(View):
    model = Submission
    template_name = 'submission_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submission = self.get_object()
        context['comments'] = submission.comments.all()
        return context

    def get(self, request, slug, *args, **kwargs):
        queryset = Submission.objects.filter(status=1)
        submission = get_object_or_404(Submission, slug=slug)
        content_type = ContentType.objects.get_for_model(Submission)
        comments = submission.comments.filter(approved=True).order_by("-created_on")
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

    def post(self, request, slug, *args, **kwargs):
        queryset = Submission.objects.filter(status=1)
        submission = get_object_or_404(queryset, slug=slug)
        title = request.GET.get('title')
        comment = None
        comments = submission.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if submission.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.submission = submission
            comment.save()
            messages.success(request, 'Your comment was submitted successfully and is waiting for admin approval')

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
        submission = get_object_or_404(Submission, slug=slug)
        if submission.likes.filter(id=request.user.id).exists():
            submission.likes.remove(request.user)
        else:
            submission.likes.add(request.user)

        return HttpResponseRedirect(reverse('submission_detail', args=[slug]))


class EditProfile(View):
    template_name = 'edit_profile.html'

    def get(self, request, *args, **kwargs):
        username = request.user.username
        email = request.user.email
        submissions = Submission.objects.filter(username_id=request.user)
        context = {'username': username, 'submissions': submissions}
        if not email:
            context['message'] = 'Please enter your email address'
        else:
            context['email'] = email
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if key.isdigit():
                submission_id = int(key)
                submission = Submission.objects.get(id=submission_id)
                submission.submission_text = value
                submission.save()
        return redirect('edit_profile')


class EditSubmission(View):
    template_name = 'edit_submission.html'

    def get(self, request, submission_id, *args, **kwargs):
        submission = get_object_or_404(Submission, id=submission_id)
        form = SubmissionForm(instance=submission)
        context = {'submission': submission, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, submission_id, *args, **kwargs):
        submission = get_object_or_404(Submission, id=submission_id)
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
        else:
            context = {'submission': submission, 'form': form}
            return render(request, self.template_name, context)

    def handle_no_permission(self):
        return redirect('edit_profile')


class DeleteSubmission(View):
    def get(self, request, submission_id, *args, **kwargs):
        submission = get_object_or_404(Submission, id=submission_id)
        if request.user == submission.username_id:
            submission.delete()
        return redirect('edit_profile')
