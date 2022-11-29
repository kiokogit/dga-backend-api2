import datetime
from .models import RolesModel


def get_user_roles(user_id):
    user_roles = RolesModel.objects.filter(
        user__id=user_id,
        is_active=True,
        is_deleted=False
    )
    if user_roles.exists():
        return user_roles.all()
    else:
        return []


class CreateUserRoles:

    def __init__(self, user:object, role:str, actor:str) -> None:
        self.user = user,
        self.role = role,
        self.actor_id = actor

    def actor_has_permission(self):
        if self.role in ["GENERAL MANAGER"]:
            if "SUPER USER" not in get_user_roles(self.actor_id):
                return False
            else:
                return True

        elif self.role in ["FINANCE OFFICER", "BOOKING MANAGER", "BOOKING OFFICER", "ICT OFFICER"]:
            if "GENERAL MANAGER" not in get_user_roles(self.actor_id):
                return False
            else:
                 return True

        elif self.role in ["CUSTOMER CARE", "GENERAL STAFF"]:
            if "ICT OFFICER" not in get_user_roles(self.actor_id):
                return False
            else:
                return True

        else:
            # No such a role
            return False


    def add_user_role(self):
        if not self.actor_has_permission():
            return False, "you do not have permission to assign role"
        
        __role = RolesModel.objects.filter(
            user = self.user,
            role=self.role
        ).first()
        if __role:
            if __role.is_active:
                return False, "user has that role"
            else:
                __role.is_active=True
                __role.is_deleted=False
                __role.date_deleted=None
                __role.save()
            return True, "Role updated successfully"

        try:
            RolesModel.objects.create(
                user = self.user,
                role=self.role,
                is_active=True
            )
        except Exception:
            return False, "role not added"

        return True, "role added successfully to user"

    def remove_user_role(self):
        if not self.actor_has_permission():
            return False, "you do not have permission to remove the role"
        
        role = RolesModel.objects.filter(
            user=self.user,
            role=self.role,
            is_active=True
        ).first()
        if not role:
            return False, "user does not have that role"
        else:
            role.is_active = False,  # type: ignore
            role.is_deleted=True,  # type: ignore
            role.date_deleted = datetime.datetime.now()

            role.save()
        return True, "user role removed successfully"
        
