from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("jobs/", views.jobs, name="jobs"),
    path(
        "apply/<int:job_id>/",
        views.apply_job,
        name="apply_job"
    ),
    path(
        "applications/",
        views.applications,
        name="applications"
    ),
    path("logout/", views.logout_view, name="logout"),
]