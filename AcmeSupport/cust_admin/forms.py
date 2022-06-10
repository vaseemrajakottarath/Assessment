import imp
from django import forms

class TicketForm(forms.Form):
    PRIORITY_CHOICES=(
    
    ('Urgent','Urgent'),
    ('Medium','Medium')
    ('low','low'),
    )

    subject=forms.CharField(widget=forms.textarea(attrs={
        'class':'form-control col-12 mb-3',
        'row':'5',
        'placeholder':'subject',
    }),label='')

    Body=forms.CharField(max_length=200)
    priority=forms.ChoiceField(choices=PRIORITY_CHOICES,widget=forms.Select(attrs={
        'class':'form-control col-12 mb-3',
        'placeholder':'department',
    }),label='')

    class Meta:
        fields=['subject','priority']