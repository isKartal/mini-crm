from django import forms
from .models import Customer, Deal, Note

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['customer', 'title', 'amount', 'status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DealForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['customer'].queryset = Customer.objects.filter(created_by=user)

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Notunuzu buraya yazın...'}),
        }
