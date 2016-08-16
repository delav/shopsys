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


# 添加商品到购物车的表单
class ProductAddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(
        label='数量',
        widget=forms.TextInput(attrs={
            'size': '2', 'value': '1', 'class': 'quantity', 'max_length': '5'}),
        error_messages={'invalid': '请输入有效数量', 'min_value': '1'})
    product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    # 检查用户浏览器端cookie是否开启
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError('需要启用cookie')
            return self.cleaned_data
