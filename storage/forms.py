from django import forms
from models import Employee, CheckIn
from models import Order
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class user_form(UserCreationForm):
    name = forms.CharField(max_length=50)
    is_lineCh = forms.BooleanField(required=False, label="LineChief")
    is_qtCh = forms.BooleanField(required=False, label="Quality")
    category = forms.IntegerField(required=False)
    line = forms.IntegerField(required=False)
    is_production = forms.BooleanField(required=False, label="Production")
    is_storage = forms.BooleanField(required=False, label="Storage")

class order_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(order_form, self).__init__(*args, **kwargs)
        # self.fields['or_delivery'].queryset=Employee.objects.filter(is_storage=True)
        # self.fields['or_receive'].queryset=Employee.objects.filter(is_production=True)
        # self.fields['or_lineCh'].queryset=Employee.objects.filter(is_lineCh=True)

    class Meta:
        model = Order
        fields = ['or_delivery', 'or_receive','or_lineCh', 'or_pieces' ]
        labels = {'or_delivery': 'Delivered ', 'or_receive': 'Received ', 'or_lineCh': 'LineChief ',
        'or_status':'Status ', 'or_pieces':'Quantity ' }
        widgets = {'or_delivery': forms.Select, 'or_receive': forms.Select, 'or_lineCh': forms.Select}


'''
class check_In(ModelForm):
    class Meta:
        model = CheckIn
        fields = ['ck_Employee']
'''
