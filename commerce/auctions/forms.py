from django import forms

class ListingForm(forms.Form):
    title = forms.CharField(label='title', max_length=150)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    price = forms.DecimalField()
    listing_date = forms.DateField()
    image = forms.URLField()