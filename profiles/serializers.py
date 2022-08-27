from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 124 *1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB.'
            )
        if value.image.width > 2063:
            raise serializers.ValidationError(
                'Image width larger than 4000px.'
            )
        if value.image.height > 3131:
            raise serializers.ValidationError(
                'Image height larger than 4000px.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "writer",
            "artist",
            "letterer",
            "colorist",
            "editor",
            "is_owner",
        ]
