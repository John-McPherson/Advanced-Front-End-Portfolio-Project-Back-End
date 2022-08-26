from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Project
        fields = [
            'id', 'owner', 'created_at', 'color','pages','updated_at', 'title',  'writers', 'artists', 'letterers','editors', 'is_owner'
        ]


