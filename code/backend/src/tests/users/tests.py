import pytest

from apps.users.models import User
from tests.common.tests import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_soft_delete_user(self, soft_deleted_user):
        user_pk = soft_deleted_user.pk
        assert self.is_soft_deleted(User, user_pk)

    def test_restore_user_through_instance(self, soft_deleted_user):
        soft_deleted_user.restore()
        assert not self.is_soft_deleted(User, soft_deleted_user.pk)

    def test_restore_user_through_manager(self, soft_deleted_user):
        User.objects_all.filter(pk=soft_deleted_user.pk).restore()
        assert not self.is_soft_deleted(User, soft_deleted_user.pk)

    def test_hard_delete_user_through_instance(self, user):
        user_pk = user.pk
        user.hard_delete()
        assert self.is_hard_deleted(User, user_pk)

    def test_hard_delete_user_through_manager(self, user):
        user_pk = user.pk
        User.objects.filter(pk=user_pk).hard_delete()
        assert self.is_hard_deleted(User, user_pk)

    def test_hard_delete_user_through_all_manager(self, user):
        user_pk = user.pk
        User.objects_all.filter(pk=user_pk).hard_delete()
        assert self.is_hard_deleted(User, user_pk)

    def test_alive_and_delete(self, random_users):
        alive_count_before_soft_delete = User.objects_all.alive().count()
        deleted_count_before_soft_delete = User.objects_all.deleted().count()
        assert (
            alive_count_before_soft_delete == len(random_users) and
            (alive_count_before_soft_delete + deleted_count_before_soft_delete) == User.objects_all.count() and
            alive_count_before_soft_delete == User.objects.count()
        )

    def test_all_soft_delete(self, random_users):
        total_count_before_soft_delete = User.objects_all.count()
        User.objects.delete()
        assert (
            User.objects.count() == 0 and
            User.objects_all.count() == total_count_before_soft_delete
        )

    def test_all_restore(self, random_users):
        User.objects.delete()
        soft_deleted_count_before_restore = len(random_users)
        User.objects_all.restore()
        assert User.objects.count() == soft_deleted_count_before_restore

    def test_all_delete_through_manager(self, random_users):
        User.objects.hard_delete()
        assert User.objects_all.count() == 0

    def test_all_delete_through_all_manager(self, random_users):
        User.objects_all.hard_delete()
        assert User.objects_all.count() == 0
