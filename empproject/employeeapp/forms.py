from django import forms
from employeeapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        labels={
            'fname':'ชื่อ',
            'lname':'นามสกุล',
            'address':'ที่อยู่',
            'gender':'เพศ',
            'birthdate':'วันเกิด',
            'department':'แผนก',
            'salary':'เงินเดือน',
            'cover':'ภาพพนักงาน'
        }
        widgets={
            'address':forms.Textarea(attrs={'rows':'3'}),
            'gender':forms.RadioSelect(),
            'birthdate':forms.DateInput(attrs={'type':'date'})
        }