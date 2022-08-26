from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import status, permissions

class ProjectList(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]



    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(
            project, many = True, context = {'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        print('before')
        serializer = ProjectSerializer(
            data=request.data, context ={'request': request}
        )
        print('after')
        print(serializer)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


