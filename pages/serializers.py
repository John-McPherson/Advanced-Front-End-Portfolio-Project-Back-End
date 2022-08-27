from rest_framework import serializers
from .models import Page


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    is_collaborator = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]

        return request.user == obj.owner

    def get_is_collaborator(self, obj):
        request = self.context["request"]

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

        return request.user == obj.owner

    class Meta:
        model = Project
        fields = [
            "id",
            "owner",
            "created_at",
            "color",
            "updated_at",
            "title",
            "writers",
            "artists",
            "letterers",
            "editors",
            "is_owner",
            "is_collaborator",
        ]
