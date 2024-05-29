from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,SAFE_METHODS
from .models import Organization, Role, User
from .serializers import OrganizationSerializer, RoleSerializer, UserSerializer
from .permissions import IsSuperAdmin, IsAdmin, IsManager, IsMember, CanRetrieveOrListOrganizations, CanUpdateOrganization, CanDeleteOrganization,CanRetrieveOrListRoles, CanCreateRole, CanUpdateRole, CanDeleteRole,CanCreateUser, CanRetrieveUser, CanUpdateUser, CanDeleteUser, CanListUsers


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permission() for permission in [IsAuthenticated, CanRetrieveOrListOrganizations]]
        if self.action == 'update':
            return [permission() for permission in [IsAuthenticated, CanUpdateOrganization]]
        if self.action == 'destroy':
            return [permission() for permission in [IsAuthenticated, CanDeleteOrganization]]
        return super().get_permissions()

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permission() for permission in [IsAuthenticated, CanRetrieveOrListRoles]]
        if self.action == 'create':
            return [permission() for permission in [IsAuthenticated, CanCreateRole]]
        if self.action in ['update', 'partial_update']:
            return [permission() for permission in [IsAuthenticated, CanUpdateRole]]
        if self.action == 'destroy':
            return [permission() for permission in [IsAuthenticated, CanDeleteRole]]
        return super().get_permissions()

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permission() for permission in [IsAuthenticated, CanCreateUser]]
        if self.action in ['retrieve', 'list']:
            return [permission() for permission in [IsAuthenticated, CanRetrieveUser if self.action == 'retrieve' else CanListUsers]]
        if self.action in ['update', 'partial_update']:
            return [permission() for permission in [IsAuthenticated, CanUpdateUser]]
        if self.action == 'destroy':
            return [permission() for permission in [IsAuthenticated, CanDeleteUser]]
        return super().get_permissions()