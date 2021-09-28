from rest_framework import serializers
from .models import File, Shared


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class SharedSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source="file.file")
    class Meta:
        model = Shared
        fields = ('file', 'code', )
