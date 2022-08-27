from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsColaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        for writer in obj.writers.all():
            if request.user == writer.owner:
                return True
        for artist in obj.artists.all():
            if request.user == artist.owner:
                return True
        for letterer in obj.letterers.all():
            if request.user == letterer.owner:
                return True
        for editor in obj.editors.all():
            if request.user == editor.owner:
                return True
        return obj.owner == request.user
