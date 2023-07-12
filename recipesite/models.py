from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Comment(models.Model):
    title = models.CharField(max_length=200, default="no title")
    name = models.CharField(max_length=100, default="anon")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    submission = models.ForeignKey('Submission', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    recipe = models.ForeignKey('Recipe', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set the related title for new comments
            if self.submission:
                self.title = self.submission.title
            elif self.recipe:
                self.title = self.recipe.title
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    comment = models.ForeignKey(Comment, related_name='recipes', on_delete=models.CASCADE, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(default='description')
    ingredients = models.TextField(default='ingredients')
    instructions = models.TextField(default='instructions')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Submission(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    comment = models.ForeignKey(Comment, related_name='submissions', on_delete=models.CASCADE, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name="submitter")
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='submission_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = 'Submissions'

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
