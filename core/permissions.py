from rest_framework import permissions


class OnlyTheOwnerAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        user = request.user

        if hasattr(obj, "account"):
            return obj.account and obj.account.user == user
        
        return False