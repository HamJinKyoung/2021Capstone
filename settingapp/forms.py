from django import forms
from main.models import Menu, CustomUser

class AddForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['m_name', 'c_id', 'm_info', 'm_img', 'm_price', 'm_takeout']

class EditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['m_name', 'c_id', 'm_info', 'm_img', 'm_price', 'm_takeout']

class CustomForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['u_id']