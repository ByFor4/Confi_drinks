from django.forms import ModelForm, TextInput
from .models import cocteil

class create_Coctail(ModelForm):
    class Meta:
        model = cocteil
        fields = ['name','description','picture']

        widgets = {
            "name": TextInput(attrs={
                #Сюда фронт
            }),
            "description": TextInput(attrs={
                # Сюда фронт
            }),
            "picture": TextInput(attrs={
                # Сюда фронт
            })
        }


