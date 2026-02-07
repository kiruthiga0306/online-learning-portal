from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
    path("enroll/<int:course_id>/", views.enroll, name="enroll"),
    path("payment/<int:course_id>/", views.make_payment, name="make_payment"),
    path("feedback/<int:course_id>/", views.feedback, name="feedback"),
    path("dashboard/", views.dashboard, name="dashboard"),
]