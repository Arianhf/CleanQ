from django.urls import path, include
from clinic import views

urlpatterns = [
    path("", views.index, name="home"),
    path("clinic/<int:pk>", views.ClinicDetailView.as_view(), name="clinic-detail"),
    path("timeslot/create", views.TimeslotCreateView.as_view(), name="timeslot-create"),
    path(
        "api/v1/",
        include(
            (
                [
                    path("", views.api_root, name="api-home"),
                    path("clinics/", views.ClinicList.as_view(), name="clinic-list"),
                    path(
                        "clinics/<int:pk>/",
                        views.ClinicDetail.as_view(),
                        name="clinic-detail",
                    ),
                    path(
                        "timeslots/", views.TimeSlotList.as_view(), name="timeslot-list"
                    ),
                    path(
                        "timeslots/<int:pk>/",
                        views.TimeSlotDetail.as_view(),
                        name="timeslot-detail",
                    ),
                    path(
                        "available-timeslots/",
                        views.availableTimeSlotsList.as_view(),
                        name="available-timeslots-list",
                    ),
                ],
                "api",
            ),
            namespace="api",
        ),
    ),
]
