from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .utils import generate_share_key
from .models import File, Shared
from .serializers import FileSerializer, SharedSerializer


class FileListAPIView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class SharedFileListAPIView(ListAPIView):
    queryset = Shared.objects.all()
    serializer_class = SharedSerializer


class FileRetrieveAPIView(RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


@api_view(['PUT'])
def edit_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    return Response("Test")


@api_view(['DELETE'])
def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    data = {"message": "file has been deleted successfully.", "code": 200}
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def share_file(request, pk):
    message = "Your file is sharable now, please sent the invitation to your collaborator."
    try:
        key = generate_share_key()
        file = get_object_or_404(File, pk=pk)
        shared_file, created = Shared.objects.get_or_create(file=file)
        shared_file.code = key
        share_file.saved()
    except:
        key = generate_share_key()
        shared_file, created = Shared.objects.get_or_create(file=file)
        shared_file.code = key
        shared_file.save()
    data = {"message": message, "code": key, "status": 200}
    return Response(data, status=status.HTTP_200_OK)
