from rest_framework import serializers


# class FileSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     upload_file = serializers.CharField()

class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    upload_file = serializers.CharField()
    file_content = serializers.CharField()
