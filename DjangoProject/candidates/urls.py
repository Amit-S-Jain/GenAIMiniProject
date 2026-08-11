# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("upload-resume/", views.upload_resume, name="upload_resume"),
    path("candidate-form/", views.candidate_form_view, name="candidate_form_view"),
]
