from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsColaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        try:
            colaborators = obj.project
        except:
            colaborators = obj

        for writer in colaborators.writers.all():
            if request.user == writer.owner:
                return True
        for artist in colaborators.artists.all():
            if request.user == artist.owner:
                return True
        for letterer in colaborators.letterers.all():
            if request.user == letterer.owner:
                return True
        for editor in colaborators.editors.all():
            if request.user == editor.owner:
                return True
        return obj.owner == request.user
