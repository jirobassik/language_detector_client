from django.urls import path
from . import views
from file_view.views import download_file

urlpatterns = [
    path('', views.show_main_view, name="view_all_data"),
    path('download_file/<int:pk>', download_file, name='file-download'),
    path('download_json_file/', views.download_json_file, name='file-download-json'),
    path('alphabet/<int:pk>', views.alphabet_method_view, name='alphabet_method'),
    path('short/<int:pk>', views.short_method_view, name='short_method'),
    path('neuro/<int:pk>', views.neuro_method_view, name='neuro_method'),
    path('alphabet/statistic/<int:pk>', views.alphabet_statistic_method_view, name='alphabet_statistic'),
    path('short/statistic/<int:pk>', views.short_statistic_method_view, name='short_statistic'),
    path('neuro/statistic/<int:pk>', views.neuro_statistic_method_view, name='neuro_statistic'),
]
