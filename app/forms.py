from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('django','DJANGO'),('sql','SQL'),('selenium','SELENIUM')]
class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #Gender=forms.ChoiceField(choices=g)
    Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
