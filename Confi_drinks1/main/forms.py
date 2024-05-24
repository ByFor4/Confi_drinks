from django.forms import ModelForm, TextInput
from .models import cocteil

class create_Coctail(ModelForm):
    class Meta:
        model = cocteil
        fields = ['name','description','picture']

        widgets = {
            "name": TextInput(attrs={
                "class": "input__title night_theme",
                "placeholder": "Имя"
            }),
            "description": TextInput(attrs={
                "class": "input__desc night_theme",
                "placeholder": "Описание"
            }),
            "picture": TextInput(attrs={
                # Сюда фронт
            })
        }


