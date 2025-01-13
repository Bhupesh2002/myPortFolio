from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message',
                'class': 'form-control',
                'rows': 5,
            }),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Please use an @gmail.com email.')
        return email
