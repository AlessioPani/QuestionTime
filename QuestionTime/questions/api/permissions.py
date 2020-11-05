from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''
    Permission that returns True if the user who made the request
    is the same who create the object or if the requested method
    is a safe one.
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author == request.user
