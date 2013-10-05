from django.forms import ModelForm
from core.models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document 
        fields = ['name','description','file']


