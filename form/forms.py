from django import forms
from django.forms import TextInput, Textarea, EmailInput

from .models import Form


# Форма
class FormOnPage(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['form_name', 'form_email', 'form_subject', 'form_text']
        widgets = {
            'form_name': TextInput(attrs={
                'placeholder': 'Ваше имя',
                'id': 'name',
                'name': 'name',
                'class': 'form-control'
            }),
            'form_email': EmailInput(attrs={
                'placeholder': 'Ваш email',
                'id': 'email',
                'name': 'email',
                'class': 'form-control'
            }),
            'form_subject': TextInput(attrs={
                'placeholder': 'Тема письма',
                'id': 'subjects',
                'name': 'subjects',
                'rows': 5,
                'class': 'form-control'
            }),
            'form_text': Textarea(attrs={
                'placeholder': 'Ваше сообщение',
                'id': 'text',
                'name': 'text',
                'class': 'form-control'
            })
        }
