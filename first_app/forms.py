from django import forms
from django.core import validators
class contactForm(forms.Form):
        name=forms.CharField(label="user Name", help_text="total 54 character",initial="rls" , required="false")
  
        # file =forms.FileField()
        # email=forms.EmailField(label="user Email")
        # age  = forms.IntegerField()
        # weight = forms.FloatField()
        # balance = forms.DecimalField()
        # check = forms.BooleanField()
        # birthday = forms.DateField()
        # appointment = forms.DateTimeField()
        # CHOICES=[("s", "Small"), ("M", "Medium"), ("L", "Large")]
        # size=forms.ChoiceField(choices=CHOICES)
        
# class StudentData(forms.Form):
#         name=forms.CharField(widget=forms.TextInput)
#         email= forms.CharField(widget=forms.EmailInput)
#         def clean_name(self):
#                 valname=self.cleaned_data['name']
#                 if len(valname)<4:
#                         raise forms.ValidationError("Enter a name with at least 4 characters")
#                 return valname
#         def clean_email(self):
#                 valEmail = self.cleaned_data['email']
#                 if '.com' not in valEmail:
                        # raise forms.ValidationError("Your email must contain .com")
                
def len_check(value):
        if len(value)<10:
                raise forms.ValidationError("Enter a value at least 10 chars")

class StudentData(forms.Form):
        name=forms.CharField(validators=[validators.MinLengthValidator(10, message="enter less than 10 character")])
        text=forms.CharField(widget=forms.TextInput, validators=[len_check])
        email= forms.CharField(widget=forms.EmailInput,  validators=[validators.EmailValidator(message='Enter a valid email address')])        
        age= forms.CharField()
        file=forms.FileField(validators=[validators.FileExtensionValidator(  allowed_extensions=['pdf', 'doc', 'docx', 'jpg'],
    message='File must be a PDF, DOC, or DOCX.',)])
        


class PasswordValidationProject(forms.Form):
        name=forms.CharField(widget=forms.TextInput)
        password=forms.CharField(widget=forms.PasswordInput)
        confirm_password=forms.CharField(widget=forms.PasswordInput)
        
        def clean(self):
                clean_data=super().clean()
                val_pass= self.cleaned_data["password"]
                val_con_pass= self.cleaned_data["confirm_password"]
                val_name=self.cleaned_data["name"]
                
                if val_pass!=val_con_pass:
                        raise forms.ValidationError("Password doesn't match")
                
        
                    
                
                
        