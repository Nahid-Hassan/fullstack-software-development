from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        print(obj.author, request.user)
        return obj.author == request.user