from django.core.urlresolvers import reverse_lazy
from core.models import Tag, Document
from core.forms import DocumentForm
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView


class ListDocuments(ListView):
    model = Document
    queryset = Document.objects.all()

    def get_queryset(self):
        print self.kwargs
        return self.queryset

class CreateDocument(CreateView):
    model = Document
    success_url = reverse_lazy('list_documents')

    def get_form(self, data=None, files=None, **kwargs):
        return DocumentForm(data, files, **kwargs)

