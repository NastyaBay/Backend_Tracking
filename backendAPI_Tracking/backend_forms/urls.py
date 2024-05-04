from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.FormListView.as_view(), name='get_forms'),
    path('forms/<str:url>/', views.FormDetailView.as_view(), name='get_single_form'),
]