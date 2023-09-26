from rest_framework import serializers


class LanguageSerializer(serializers.Serializer):
    text_language = serializers.CharField()
    filename = serializers.CharField()
    file_id = serializers.IntegerField()


class StatisticSerializer(serializers.Serializer):
    alphabet_time = serializers.CharField()
    short_time = serializers.CharField()
    neuro_time = serializers.CharField()
    english_percent = serializers.IntegerField()
    russian_percent = serializers.IntegerField()
