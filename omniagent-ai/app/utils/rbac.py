from app.config import settings

class RBAC:
    def check_access(self, action):
        role = settings.RBAC_ROLE

        permissions = {
            "admin": ["read", "write", "alert"],
            "user": ["read"],
        }

        return action in permissions.get(role, [])