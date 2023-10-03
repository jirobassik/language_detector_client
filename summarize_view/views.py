import mimetypes
import os
from django.http import HttpResponse
from django.shortcuts import render
from utils.init_json_ser_req import summarize_request, summarize_serializer
from utils.txt_usage import write_txt
from utils.queryset_upl import file_queryset_upl


def show_main_view(request):
    queryset_file = file_queryset_upl()
    return render(request, 'summarize_view/main_view.html', {'files': queryset_file})


def download_json_file(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'summarize.txt'
    filepath = base_dir + '/summarize_view/static/summarize_view/upload/' + filename
    path = open(filepath, 'r', encoding="utf-8")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def summarize_text(request, pk):
    summarize_content_request = summarize_request.detail_get_request(id=pk)
    summarize_data = summarize_serializer.decode(summarize_content_request.content, many=False)
    dict_summarize = dict(summarize_data)
    write_txt(dict_summarize)
    return render(request, 'summarize_view/sum_rez.html', {'sum_text': summarize_data})
