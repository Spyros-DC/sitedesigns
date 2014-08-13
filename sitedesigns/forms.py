# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label ='Όνομα')
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea(attrs={'cols':30, 'rows':7}), label ='Σχόλιο')
