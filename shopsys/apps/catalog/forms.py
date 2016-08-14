# coding:utf-8
from django import forms
from .models import Product


# 自定义验证
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于零')
        return self.cleaned_data['price']
