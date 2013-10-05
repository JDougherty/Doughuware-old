from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    def children(self):
        return Tag.objects.filter(parent=self.pk)

    def serializable_object(self):
        obj = {'name': self.name, 'children': []}
        for child in self.children():
            obj['children'].append(child.serializable_object())
        return obj


class Document(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/%Y/%m/%d")
    thumbnail = models.ImageField(upload_to="documents/thumbnails/%Y/%m/%d")
    preview = models.ImageField(upload_to="documents/previews/%Y/%m/%d")
