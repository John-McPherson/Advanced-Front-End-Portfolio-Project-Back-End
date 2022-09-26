from rest_framework import serializers
from .models import Page
from django.contrib.humanize.templatetags.humanize import naturaltime

class PageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    is_owner = serializers.SerializerMethodField()
    is_collaborator = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    # page_number = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()
    artists = serializers.SerializerMethodField()
    letterers = serializers.SerializerMethodField()
    editors = serializers.SerializerMethodField()
    colorists = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()


    def validate_image(self, value):
        if value.size > 124 *1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB.'
            )
        if value.image.width > 2063:
            raise serializers.ValidationError(
                'Image width larger than 2063px.'
            )
        if value.image.height > 3131:
            raise serializers.ValidationError(
                'Image height larger than 3131px.'
            )
        return value

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
        
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)



    def get_is_owner(self, obj):
        request = self.context["request"]
        print(obj.project.writers.all())

        return request.user == obj.owner

    def get_is_collaborator(self, obj):
        request = self.context["request"]

        for writer in obj.project.writers.all():
            if request.user == writer.owner:
                return True
        for artist in obj.project.writers.all():
            if request.user == artist.owner:
                return True
        for letterer in obj.project.writers.all():
            if request.user == letterer.owner:
                return True
        for editor in obj.project.writers.all():
            if request.user == editor.owner:
                return True

        return request.user == obj.owner
    
    def get_color(self,obj):
        return obj.project.color

    def get_writers(self, obj):
        writers = []
        for writer in obj.project.writers.all():
            writers.append(writer.id)

        return writers


    def get_artists(self, obj):
        artists = []
        for artist in obj.project.artists.all():
            artists.append(artist.id)

        return artists

    def get_colorists(self, obj):
        colorists = []
        for colorist in obj.project.colorists.all():
            colorists.append(colorist.id)

        return colorists


    def get_letterers(self, obj):
        letterers = []
        for artist in obj.project.letterers.all():
            letterers.append(artist.id)

        return letterers

    def get_editors(self, obj):
        editors = []
        for editor in obj.project.editors.all():
            editors.append(editor.id)

        return editors


    class Meta:
        model = Page
        fields = [
            "id",
            'page_number',
            "owner",
            "created_at",
            "updated_at",
            "title",
            'project',
            "roughs",
            "inks",
            "colors",
            "letters",
            "is_owner",
            "is_collaborator",
            "color",
            'writers',
            'artists',
            'letterers',
            'colorists',
            'editors',

        ]
