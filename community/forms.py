from django import forms
from .models import Post
from .models import Comment
from serviceapply.models import Service

class PostForm(forms.ModelForm):
    choice = forms.ChoiceField(
        choices=[(choice.pk, choice) for choice in Service.objects.all()])
    class Meta:
        model = Post
        fields = ('title','text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
