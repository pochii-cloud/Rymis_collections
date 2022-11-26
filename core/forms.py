from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Accounts.models import Profile
from Orders.models import Order, OrderCodes
from Region.models import Town
from core.models import CustomerComments


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['county', 'town', 'ordered_by', 'mobile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['town'].queryset = Town.objects.none()

        if 'county' in self.data:
            try:
                county_id = int(self.data.get('county'))
                self.fields['town'].queryset = Town.objects.filter(region_id=county_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['town'].queryset = self.instance.county.town_set.order_by('name')


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'phone', 'address']


class CustomerCommentForm(forms.ModelForm):
    class Meta:
        model = CustomerComments
        fields = ['comment']


class OrderCodeForm(forms.ModelForm):
    class Meta:
        model = OrderCodes
        fields = ['code']

