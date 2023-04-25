from django import forms


class Contactform(forms.Form):
    Name = forms.CharField(max_length=100, help_text="Enter your name")
    email = forms.EmailField(help_text='Enter your email')
  #../email  Gender = forms.RadioSelect(choices="gender {male,female,others}")
    file = forms.FileField()
    message = forms.CharField(widget=forms.Textarea, help_text='Enter your Message')
