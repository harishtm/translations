from django import forms
from models import Register

class Register_Form(forms.ModelForm):
    class Meta:
        model = Register