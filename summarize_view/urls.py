from django.urls import path
from . import views
from file_view.views import download_file

urlpatterns = [
    path('', views.show_main_view, name="view_all_data"),
    path('download_file/<int:pk>', download_file, name='file-download'),
    path('download_json_file/', views.download_json_file, name='file-download-json'),
    path('summarize_neuro/<int:pk>', views.summarize_text, name='sum-text-neuro'),
]
