from django import forms


# class MultiChoice(forms.Form):

#     choices = forms.MultipleChoiceField(
#             widget=forms.CheckboxSelectMultiple,
#             choices= EXPERIENCE_CHOICES,
#         )

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)