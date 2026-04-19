from django import forms
from .models import ContactMessage
from captcha.fields import CaptchaField
class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
