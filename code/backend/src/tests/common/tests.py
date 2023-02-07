import pytest
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from apps.common.permissions import GroupPermissionsService
from apps.users.models import User


@pytest.mark.django_db
class BaseTestCase:
    @staticmethod
    def is_soft_deleted(model_class, pk):
        return (
            model_class.objects_all.filter(pk=pk, deleted_at__isnull=False).exists() and
            not model_class.objects.filter(pk=pk).exists() and
            not model_class.objects_all.alive().filter(pk=pk).exists() and
            model_class.objects_all.deleted().filter(pk=pk).exists()
        )

    @staticmethod
    def is_hard_deleted(model_class, pk):
        return not model_class.objects_all.filter(pk=pk).exists()


class TestGroupPermissions(BaseTestCase):
    def test_group_creation_with_permissions(self, group_name, permissions):
        group_permissions_service = GroupPermissionsService()

        group_permissions_service.group_permissions = [
            {
                'group_name': group_name,
                'content_type_model': User,
                'permissions': permissions,
            },
        ]
        group_permissions_service.add_permissions_to_group(None)
        group = Group.objects.filter(name=group_name).first()
        group_permissions = group.permissions.values_list('codename', flat=True)
        assert (
            (group is not None) and
            all([permission in group_permissions for permission in permissions])
        )
