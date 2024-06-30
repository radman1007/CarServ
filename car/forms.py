from django import forms
from .models import Contact,Service,Comment,News

class ServiceNameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    service = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        
class NewsNameForm(forms.Form):
    email = forms.EmailField()
 
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['email']
        
        
class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class CommentNameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name' , 'email' , 'message']