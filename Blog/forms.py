from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
                            attrs={
                            'placeholder': 'Enter a New title'
                            }
                        )
                    )
    content = forms.Textarea(attrs={
                            'placeholder': 'Enter content with love',
                            'rows'       : 40,
                            'cols'       : 160
                            }
                        )
    class Meta:
        model = Article
        fields = (
            "title",
            'content',
            'active'
        )

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title == 'abc':
            raise forms.ValidationError("Invalid Input")
        else:
            return title
