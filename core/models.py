from django.db import models
from accounts.models import User
# Create your models here.

class Document(models.Model):
    TYPE_CHOICES = (
        ("Note", "Note"),
        ("Task", "Task"),
        ("Document", "Document")
    )
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Ongoing", "Ongoing"),
        ("Done", "Done")
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=250, choices=TYPE_CHOICES, default="Note")
    status = models.CharField(max_length=250, choices=STATUS_CHOICES, default="Pending", null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    document_guid = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)
