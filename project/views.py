from django.http import Http404
from rest_framework import status , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from makecomics_api.permissions import  IsColaborator
from .models import Project
from .serializers import ProjectSerializer


class ProjectList(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        print("before")
        serializer = ProjectSerializer(data=request.data, context={"request": request})
        print("after")
        print(serializer)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsColaborator]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(
            project, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
