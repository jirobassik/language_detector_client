from rest_framework import serializers

class SummarizeSerializer(serializers.Serializer):
    sum_text = serializers.CharField()
    sum_text_standart = serializers.CharField()
    key_words = serializers.CharField()
    filename = serializers.CharField()
    file_id = serializers.IntegerField()
