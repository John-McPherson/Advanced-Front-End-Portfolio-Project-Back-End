from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Page
from .serializers import PageSerializer
from rest_framework import status, permissions, generics
from django_filters.rest_framework import DjangoFilterBackend
from makecomics_api.permissions import IsOwnerOrReadOnly, IsColaborator


class PageList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project", "title"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PageDetail(APIView):
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            page = Page.objects.get(pk=pk)
            self.check_object_permissions(self.request, page)
            return page
        except Page.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        page = self.get_object(pk)
        serializer = PageSerializer(page, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        print(self)
        page = self.get_object(pk)
        serializer = PageSerializer(
            page, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        page = self.get_object(pk)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
