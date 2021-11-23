from django import forms
from .models import  PostModel, Comment


class PostModelForm(forms.ModelForm):
    class Meta: 
        model = PostModel
        fields = ["titolo","contenuto","argomento"]
        #widgets = {"contenuto":Textarea(attrs={"rows":"5"})} 
        labels = {"contenuto": "Messaggio"}


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['contenuto_commento']