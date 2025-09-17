from rest_framework import viewsets
from ..models.asiento_contable import AsientoContable
from ..serializers.asiento_contable import AsientoContableSerializer
from rest_framework.permissions import IsAuthenticated

class AsientoContableViewSet(viewsets.ModelViewSet):
    queryset = AsientoContable.objects.all()
    serializer_class = AsientoContableSerializer
    permission_classes = [IsAuthenticated]
    