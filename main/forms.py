from django import forms
from django.utils.html import strip_tags
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "thumbnail",
            "category",
            "is_featured",
            "stock",
            "is_official_merch",
            "size",
            "is_signed",
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter product name",
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
                "placeholder": "Enter price",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter product description",
                "rows": 3,
            }),
            "thumbnail": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com/image.jpg",
            }),
            "category": forms.Select(attrs={
                "class": "form-select",
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
            }),
            "is_official_merch": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
            "size": forms.Select(attrs={
                "class": "form-select",
            }),
            "is_signed": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()
        return strip_tags(description)

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get("thumbnail", "").strip()
        return strip_tags(thumbnail)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None or price < 0:
            raise forms.ValidationError("Price cannot be empty or negative.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is None or stock < 0:
            raise forms.ValidationError("Stock cannot be empty or negative.")
        return stock
