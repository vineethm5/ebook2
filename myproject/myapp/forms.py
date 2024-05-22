from django import forms
from .models import ebookss

class ebookforms(forms.ModelForm):
    CATEGORY_CHOICES =[
        ('Education','Education'),
        ('Fiction','Fiction'),
        ('Science','Science'),

    ]
    category=forms.ChoiceField(choices=CATEGORY_CHOICES)

class Meta:
    Model=ebookss
    fields=['title','summary','pages','pdf','category']

def __init__(self,*args,**kwargs):
    super(ebookforms,self).__init__(*args,*kwargs) #even  though you dont have init method in your parent class, we are overriding here, becouse our parent class is being inherited from forms.Modlesforms class, so that class have its own init
    self.fields['title'].widget.attrs.update({'class':'form-control'},{'placeholder':'enter the title'})
    self.fields['summary'].widget.attrs.update({'class':'form-control'},{'placeholder':'Enter summary'})
    self.feilds['pages'].widget.attrs.update({'class':'form-control'},{'placeholder':'Enter pages'})
    self.feilds['pdf'].widget.attrs.update({'class':'form-control'},{'placeholder':'Enter pdf'})
    self.feilds['category'].wiget.attrs.update({'class':'form-control'},{'placeholder':'Select category'})

    for field_name, field in self.fields.items():
            field.required = True

