from django import forms
from Work.models import User,Taskmodel

class Register(forms.ModelForm):

    class Meta:

           model= User
           fields= ['username',"first_name","last_name","email","password"] 
           widgets={
                'username':forms.Textarea(attrs={'class':'form-control','column':4,"rows":1,'placeholder':'enter the username'}),
                'first_name':forms.Textarea(attrs={'class':'form-control','column':4,"rows":1,'placeholder':'enter the frist_name'}),
                'last_name':forms.Textarea(attrs={'class':'form-control','column':4,"rows":1,'placeholder':'enter the last_name'}),
                'email':forms.Textarea(attrs={'class':'form-control','column':4,"rows":1,'placeholder':'enter the email'}),
                'password':forms.Textarea(attrs={'class':'form-control','column':4,"rows":1,'placeholder':'enter the password'}),

           }

class TaskForm(forms.ModelForm):
    
    class Meta:

            model= Taskmodel
            fields= ["task_name","task_description"] 
            widgets={
                'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the task'}),
                'task_description':forms.Textarea(attrs={'class':'form-control','column':20,"rows":5,'placeholder':'enter a description'})

            }

class LoginForm(forms.Form):
     username=forms.CharField()
     password=forms.CharField()

  

