from django.conf.urls import patterns, include, url
from core.models import Document
from core.views import ListDocuments

urlpatterns = patterns(
    '',
    url(r'^$', ListDocuments.as_view(), name="list_documents"),
)
