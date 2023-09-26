import json
import mimetypes
import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import cgi
from utils.init_json_ser_req import download_request, language_detector_serializer, language_short_request, \
    language_neuro_request, language_alphabet_request, statistic_request, statistic_serializer
from utils.queryset_upl import file_queryset_upl
from utils.json_usage import write_json

def main_view(request):
    return show_main_view(request)


def show_main_view(request):
    queryset_file = file_queryset_upl()
    return render(request, 'lang_view/main_view.html', {'files': queryset_file})


def alphabet_method_view(request, pk):
    alphabet_content_request = language_alphabet_request.detail_get_request(id=pk)
    return detector_language_view(alphabet_content_request, request, 'алфавитный')


def short_method_view(request, pk):
    short_content_request = language_short_request.detail_get_request(id=pk)
    return detector_language_view(short_content_request, request, 'коротких слов')


def neuro_method_view(request, pk):
    neuro_content_request = language_neuro_request.detail_get_request(id=pk)
    return detector_language_view(neuro_content_request, request, 'нейросетевой')


def detector_language_view(content_request, request, method):
    if content_request.status_code == 200:
        language = language_detector_serializer.decode(content_request.content,
                                                       many=False)
        statistic_raw_data = statistic_request.get_request()
        statistic_result = statistic_serializer.decode(raw_data=statistic_raw_data, many=False)
        json_dict_result = dict(language) | {"method": method} | dict(statistic_result)
        write_json(json_dict_result)
        return render(request, 'lang_view/language.html',
                      {'language': language, 'method': method, 'statistic': statistic_result})
    return HttpResponseRedirect(reverse('view_all_data'))


def download_json_file(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'statistic.json'
    filepath = base_dir + '/lang_view/static/lang_view/upload/' + filename
    path = open(filepath, 'r', encoding="utf-8")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
