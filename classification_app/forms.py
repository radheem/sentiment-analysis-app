from django import forms 
  
class Classify(forms.Form): 
    text = forms.CharField()
    sentiment = forms.Textarea()   
    class Meta: 
        fields = ['text']