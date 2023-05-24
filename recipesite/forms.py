from .models import Comment, Post, Submission, Page
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    page = forms.ModelChoiceField(queryset=Page.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'description', 'ingredients', 'instructions', 'page']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SubmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Submission
        fields = ('title', 'description', 'ingredients', 'instructions',)
