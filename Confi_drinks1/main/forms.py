from .models import user
from django.forms import ModelForm, TextInput

class userForms(ModelForm):
    class Meta:
        model = user
        fields = ["name","password"]

        widgets = {
            "name": TextInput(attrs={
                "class": "register__button-input",
                "placeholder": "a"
                }),
            "password": TextInput(attrs={
                "class": "register__button-input",
                "placeholder": "a"
            }),
            }

