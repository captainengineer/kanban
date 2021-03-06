from django import forms
from django.contrib.auth.models import User
from .models import List, Card # 追記

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email", )

# ここから追記
class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ("title",)
# ここまで追記

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description", "list")


class CardCreateFromHomeForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description",)