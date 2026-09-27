from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ["display_name"]
        labels = {"display_name": "Ваше имя"}
        widgets = {
            "display_name": forms.TextInput(
                attrs={
                    "placeholder": "Введите имя",
                    "autocomplete": "off",
                }
            )
        }

    def clean_display_name(self):
        display_name = self.cleaned_data["display_name"].strip()

        if not display_name:
            raise forms.ValidationError("Поле имени не должно быть пустым.")

        if not any(char.isalpha() for char in display_name) or not all(
            char.isalpha() or char in " -" for char in display_name
        ):
            raise forms.ValidationError(
                "Имя может содержать только буквы, пробелы и дефис."
            )

        return display_name
