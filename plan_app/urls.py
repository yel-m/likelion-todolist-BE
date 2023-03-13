from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>", views.Plans.as_view()),
    path("<str:username>/<int:id>", views.PlanDetail.as_view()),
    path("<str:username>/<int:id>/check", views.PlanCheck.as_view()),
    path("<str:username>/<int:id>/reviews", views.PlanReview.as_view()),
]