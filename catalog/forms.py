from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "photo", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите названние продукта"})

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["photo"].widget.attrs.update({"class": "form-control", "placeholder": "Загрузите изображение"})

        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену товара"})

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена товара не должна быть отрицательной")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for i in settings.BANNED_LIST:
            if name.lower().count(i) > 0 or description.lower().count(i) > 0:
                raise ValidationError(
                    f"В названии или описании не должны находиться запрещенные слова: {settings.BANNED_LIST}"
                )
        return cleaned_data
