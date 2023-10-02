from file_view.serializers import FileSerializer
from file_view.models import FileModel
from summarize_view.models import SummarizeModel
from summarize_view.serializers import SummarizeSerializer

from utils.request_server import Request
from utils.json_serializer import JsonSerializer

file_json_serializer = JsonSerializer(FileModel, FileSerializer)
file_request = Request.uploadfiles_model()

summarize_serializer = JsonSerializer(SummarizeModel, SummarizeSerializer)
summarize_request = Request.summarize_model()

download_request = Request.download_model()
