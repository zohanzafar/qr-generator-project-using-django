from django import forms

class QRCodeForm(forms.Form):
    url = forms.URLField(label='Enter URL', max_length=200, required=True, widget=forms.URLInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 my-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': 'Enter the url/link',}))


    