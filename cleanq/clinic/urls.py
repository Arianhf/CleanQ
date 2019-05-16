from django.urls import path
from clinic import views

urlpatterns = [
    path("", views.api_root),
    path("clinics/", views.ClinicList.as_view(), name="clinic-list"),
    path("clinics/<int:pk>/", views.ClinicDetail.as_view(), name="clinic-detail"),
    path("timeslots/", views.TimeSlotList.as_view(), name="timeslot-list"),
    path("timeslots/<int:pk>/", views.TimeSlotDetail.as_view(), name="timeslot-detail"),
    path("user/", views.BasicUserList.as_view(), name="user-list"),
    path("user/<int:pk>/", views.BasicUserDetail.as_view(), name="user-detail"),
    path(
        "representative/",
        views.ClinicRepresentativeList.as_view(),
        name="clinicrepresentative-list",
    ),
    path(
        "representative/<int:pk>/",
        views.ClinicRepresentativeDetail.as_view(),
        name="clinicrepresentative-detail",
    ),
]

