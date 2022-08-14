from django import forms




class UserMessage(forms.Form):

    name = forms.CharField(max_length=225)
    phone = forms.CharField(max_length=225)
    from_email = forms.EmailField(required=True)
    message = forms.CharField( widget=forms.Textarea ,required=True)

