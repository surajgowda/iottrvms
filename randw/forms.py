from django import forms
from .models import CustomUser
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'  # You can specify specific fields if needed
