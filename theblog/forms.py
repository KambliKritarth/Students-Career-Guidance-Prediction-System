from django import forms
from .models import Comment
# creating a form
class InputForm(forms.Form):
 
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )

'''class QueryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'Name': forms.TextInput(attrs = {'class':'form-control'}),
            'body':forms.Textarea(attrs = {'class':'form-control'}),
        }'''