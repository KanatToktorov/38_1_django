from django import forms
from product.models import Product, Review


# class ProductForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         min_length=2,
#         required=True,
#         label='Наименование',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите наименование'
#             }
#         )
#     )
#     description = forms.CharField(
#         label='Описание',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите описание'
#             }
#         )
#     )
#     image = forms.ImageField(
#         required=False,
#         label='Изображение',
#         widget=forms.FileInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if 'python' in title:
    #         # self.errors['title'] = ['Python в наименовании недопустим!']
    #         raise forms.ValidationError('Python в наименовании недопустим!')
    #
    #     return title

    # def clean(self):
    #     title = self.cleaned_data.get('title')
    #     description = self.cleaned_data.get('description')
    #
    #     if title == description:
    #         raise forms.ValidationError('Наименование и описание не должны совпадать!')
    #
    #     return self.cleaned_data


class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите наименование'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'title': 'Наименование',
            'description': 'Описание',
            'image': 'Изображение'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']