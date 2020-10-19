from django import forms
from .models import Post
from .models import Comment
from serviceapply.models import Service


class PostForm(forms.ModelForm):
    service = forms.ChoiceField(
        choices=[(choice.pk, choice) for choice in Service.objects.all()])
    work_hardness = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min' : '1', 'max':'9'}))
    work_happyness = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min' : '1', 'max':'9'}))
    work_env = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min' : '1', 'max':'9'}))
    night_work_frequency = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min' : '1', 'max':'9'}))
    self_dev = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min' : '1', 'max':'9'}))

    class Meta:
        model = Post
        fields = ('title', 'text', 'service','work_hardness', 'work_happyness', 'work_env', 'night_work_frequency', 'self_dev')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
