from django.urls import path
from . import views

urlpatterns = [
    path("", views.Plans.as_view()),
    path("<int:id>", views.PlanDetail.as_view()),
]