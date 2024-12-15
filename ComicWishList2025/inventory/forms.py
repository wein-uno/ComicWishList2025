from django import forms
from .models import Comic

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'number', 'grade', 'price']  # Exclude 'image' from the fields
        # Keep the image input as an additional field for upload
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
