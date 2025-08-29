from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('título', 'texto', 'archivo')
        widgets = {
            'archivo': forms.FileInput(attrs={
                'accept': 'image/*,video/*',
                'class': 'form-control-file'
            }),
            'título': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido del post',
                'rows': 5
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('autor', 'texto')
        widgets = {
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario',
                'rows': 3
            })
        }