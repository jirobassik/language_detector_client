from file_view.serializers import FileSerializer
from file_view.models import FileModel
from lang_view.models import LanguageDetectorModel, StatisticModel
from lang_view.serializers import LanguageSerializer, StatisticSerializer

from utils.request_server import Request
from utils.json_serializer import JsonSerializer

file_json_serializer = JsonSerializer(FileModel, FileSerializer)
file_request = Request.uploadfiles_model()

language_detector_serializer = JsonSerializer(LanguageDetectorModel, LanguageSerializer)
language_alphabet_request = Request.alphabet_model()
language_short_request = Request.short_model()
language_neuro_request = Request.neuro_model()

statistic_serializer = JsonSerializer(StatisticModel, StatisticSerializer)
statistic_request = Request.statistic_model()

download_request = Request.download_model()
