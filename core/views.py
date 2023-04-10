from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer

# Create your views here.
class DocumentViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.filter(author=self.request.user)
        type = self.request.query_params.get('type', None)
        status = self.request.query_params.get('status', None)
        if type is not None :
            queryset = queryset.filter(type=type.capitalize())
        if status is not None :
            queryset = queryset.filter(status=status.capitalize())
        return queryset
