from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(forms.Form):
	user_email = forms.CharField(max_length=100,required=True)
	user_password = forms.CharField(max_length=100,required=True)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-LoginForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = ''
		self.helper.add_input(Submit('login', 'Login'))
