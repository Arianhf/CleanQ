from django.urls import path, include
from clinic import views

urlpatterns = [
    path("", views.api_root),
    path("clinics/", views.ClinicList.as_view(), name="clinic-list"),
    path("clinics/<int:pk>/", views.ClinicDetail.as_view(), name="clinic-detail"),
    path("timeslots/", views.TimeSlotList.as_view(), name="timeslot-list"),
    path("timeslots/<int:pk>/", views.TimeSlotDetail.as_view(), name="timeslot-detail"),
    path("basic-users/", views.BasicUserList.as_view(), name="basicuser-list"),
    path(
        "basic-users/<int:pk>/",
        views.BasicUserDetail.as_view(),
        name="basicuser-detail",
    ),
    path(
        "representatives/",
        views.ClinicRepresentativeList.as_view(),
        name="clinicrepresentative-list",
    ),
    path(
        "representatives/<int:pk>/",
        views.ClinicRepresentativeDetail.as_view(),
        name="clinicrepresentative-detail",
    ),
    path("rest-auth/", include("rest_auth.urls")),
    path("users/", include("users.urls")),
]

