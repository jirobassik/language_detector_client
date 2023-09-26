from django.urls import path
from . import views
from file_view.views import download_file

urlpatterns = [
    path('', views.main_view, name="view_all_data"),
    path('download_file/<int:pk>', download_file, name='file-download'),
    path('download_json_file/', views.download_json_file, name='file-download-json'),
    path('alphabet/<int:pk>', views.alphabet_method_view, name='alphabet_method'),
    path('short/<int:pk>', views.short_method_view, name='short_method'),
    path('neuro/<int:pk>', views.neuro_method_view, name='neuro_method'),
]
