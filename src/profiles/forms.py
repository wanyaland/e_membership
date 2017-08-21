from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            )

    class Meta:
        model = User
        fields = ['name']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            Field('bio'),
            Field('date_of_birth'),
            Field('nationality'),
            Field('country_of_residence'),
            Field('marital_status'),
            Field('town'),
            Field('village'),
            Field('national_id_doc'),
            Field('national_id'),
            Field('subscription'),
            Field('email'),
            Field('telephone'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio','date_of_birth','nationality','country_of_residence','marital_status','town','village','national_id_doc','national_id','email','telephone',
                  'subscription']
