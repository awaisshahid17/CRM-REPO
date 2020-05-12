from django import forms
from .models import Promocode
from crm_manager.models import Promocode, Calculator, Code
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password


class CodeForm(forms.ModelForm):
    name = forms.CharField(required=True,
                            error_messages={'required': 'Enter Name'},
                            widget=forms.TextInput
                            (attrs={'class': 'form-control', 'placeholder': 'Name'})
                            )
    email = forms.CharField(required=True,
                                  error_messages={'required': 'Enter email '},
                                  widget=forms.TextInput
                                  (attrs={'class': 'form-control', 'placeholder': 'Email'})
                                  )
    phone = forms.CharField(required=True,
                                        error_messages={'required': 'Enter Phone '},
                                        widget=forms.TextInput
                                        (attrs={'class': 'form-control', 'placeholder': 'Phone'})
                                        )

    age = forms.IntegerField(required=True,
                            error_messages={'required': 'Enter Age '},
                            widget=forms.TextInput
                            (attrs={'class': 'form-control', 'placeholder': 'Age'})
                            )

    class Meta:
        model = Code
        fields = ["name",'email','phone','age','status']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            }

class CalculatorForm(forms.ModelForm):

    class Meta:
        model = Calculator
        fields = ['user']


class PromocodeForm(forms.ModelForm):

    code = forms.CharField(required=True,
                           error_messages={'required': 'Enter Code'},
                           widget=forms.TextInput
                           (attrs={'class': 'form-control', 'placeholder': 'Code'})
                           )
    amount_percent = forms.CharField(required=True,
                                     error_messages={'required': 'This field is required'},
                                     widget=forms.TextInput
                                     (attrs={'class': 'form-control', 'placeholder': 'amount_percent'})
                                     )

    class Meta:
        model = Promocode
        fields = ["code", 'type', 'amount_percent', 'is_free', 'is_Available']

    widgets = {
        'code': forms.TextInput(attrs={'class': 'form-control'}),
        'amount_percent': forms.TextInput(attrs={'class': 'form-control'}),
    }

    def clean_amount_percent(self):
        type = self.cleaned_data["type"]
        amount = int(self.cleaned_data["amount_percent"])
        if type == "percent":
            print type, amount
            if amount < 0 or amount > 100:
                print "ValidationError"
                raise ValidationError("Value should be  0 to 100")
            else:
                amount = 100-amount
                print "amount", amount
                return amount
        return self.cleaned_data["amount_percent"]
