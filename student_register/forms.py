from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= ('fullname','stu_code','mobile','stream')
        labels= {
            'fullname':'Full Name',
            'stu_code': 'Student Code',
           }
    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)    
        self.fields['stream'].empty_label="Select"
        self.fields['stu_code'].required= False   
    
   
