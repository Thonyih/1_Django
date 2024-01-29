from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                            "placeholder": "a title here"
                                        }
                                    )
                                    )

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if title.isdigit():
            raise forms.ValidationError("Not a valid title")
        return title
    





class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                            "placeholder": "a title here"
                                        }
                                    )
                                    )

    description = forms.CharField(required=False, 
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "a description here",
                                          "class": "new-class-name two",
                                          "rows": 10,
                                          "cols": 20,
                                      }
                                  )
                                  )
    
    price = forms.DecimalField(initial=199.99)
