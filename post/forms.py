from django import forms

from post.models import Product, Comment, Category


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content', 'photo', 'rate') # Поля которые мы хоти видеть взятые из моделек


class CategoryCreateForm(forms.ModelForm):
    class Meta: # Мы можем указать класс который хотим унасследовать
        model = Category
        fields = ('title',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
