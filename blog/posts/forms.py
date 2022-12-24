from django import forms
from django.core.exceptions import ValidationError

from .models import Group, Post


class GroupForm(forms.ModelForm):
    def clean_slug(self):
        cleaned_slug = self.cleaned_data["slug"].lower()
        if cleaned_slug == "new":
            raise ValidationError("A slug may not be a 'new'")
        return cleaned_slug

    class Meta:
        model = Group
        fields = ("title", "slug", "description")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'group', 'text')

        labels = {
            'text': 'Текст',
            'topic': "Тема",
            'group': 'Группа'
        }

        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост',
            'topic': "Тема поста"
        }

        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

    def clean_topic(self):
        cleaned_topic = self.cleaned_data["topic"].lower()
        if cleaned_topic == "new topic":
            raise ValidationError("A topic may not be a 'new'")
        return cleaned_topic
