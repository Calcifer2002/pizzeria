from django import forms
from .models import *
from django.forms import TextInput
 # import all of your models

class Pizzaform(forms.ModelForm):
      class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese']
      toppings = forms.ModelMultipleChoiceField(
        queryset=Topping.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
class Orderform(forms.ModelForm):
    # Form meta info
    class Meta:
        model = Order
        fields = ["name", "address", "cardNum", "expiration", "cvv"]
        widgets = {
            'expiration': TextInput(attrs={'type': 'text', 'pattern': '(0[1-9]|1[0-2])\/\d{2}', 'value': '01/02'}),
            
        }

    def clean(self):
        data = self.cleaned_data
        name = data.get("name")
        address = data.get("address")
        number = data.get("cardNum")
        exp = data.get("expiration")
        cvv = data.get("cvv")

        errorsList = []  # create an empty list to store errors

        if not name:
            errorsList.append(forms.ValidationError("Please enter a name."))
        if not address:
            errorsList.append(forms.ValidationError("Please enter an address."))
        if not number:
            errorsList.append(forms.ValidationError("Please enter a card number."))
        elif len(number) < 19 & len(number) > 10| len(number)> 19:
            errorsList.append(forms.ValidationError("Not a valid card number!"))
        else:
           try:
              int(number)
           except ValueError:
              errorsList.append(forms.ValidationError("Please enter a valid integer for the card number."))

        if not exp:
            errorsList.append(forms.ValidationError("Please enter an expiration date."))
        elif len(exp) != 5 or exp[2] != '/':
            errorsList.append(forms.ValidationError("Expiration date should be in the format MM/YY."))
        else:
            try:
              int(exp[:2])
              int(exp[3:])
            except ValueError:
              errorsList.append(forms.ValidationError("Please enter a valid expiration date."))
        
        if not cvv:
            errorsList.append(forms.ValidationError("Please enter a CVV."))
        elif len(cvv) != 3:
            errorsList.append(forms.ValidationError("CVV not valid!"))
        else:
           try:
              int(cvv)
           except ValueError:
              errorsList.append(forms.ValidationError("Please enter a valid integer for the cvv."))
        if errorsList:
            raise forms.ValidationError(errorsList)
        
        return data

