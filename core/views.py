from django.core.urlresolvers import reverse_lazy
from core.models import Tag,Document
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView

class ListDocuments(ListView):
    model = Document
