from django.urls import path
from . import views

app_name = "assessment"

urlpatterns = [
    path("", views.home, name="home"),
    path("assess/", views.questionnaire, name="questionnaire"),
    path("result/<int:assessment_id>/", views.result, name="result"),
]
