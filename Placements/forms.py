from django import forms
from .models import Companies
class CompanyForm(forms.Form):
    company_form= forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Select Company", to_field_name="name")
