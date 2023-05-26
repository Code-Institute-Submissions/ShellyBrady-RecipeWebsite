from .models import Comment, Post, Submission, MemberRecipe
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
