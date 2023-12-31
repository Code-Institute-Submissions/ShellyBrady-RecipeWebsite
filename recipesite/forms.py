from .models import Comment, Recipe, Submission
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'style':
                                                        'height: 100px;'}))

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
