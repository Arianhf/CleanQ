from django.urls import path, include
from clinic import views
from users.views import user as user_views

urlpatterns = [
    path("", views.index, name="home"),
    path("reserve-timeslot/", views.reserve_slot, name="reserve-timeslot"),
    path(
        "clinic/<int:pk>/", views.ClinicDetailView.as_view(), name="clinic-detail-view"
    ),
    path(
        "clinic/<int:pk>/reserve-timeslot/",
        views.reserve_slot_clinic,
        name="clinic-reserve-timeslot",
    ),
    path(
        "timeslot/create/", views.TimeslotCreateView.as_view(), name="timeslot-create"
    ),
    path(
        "my-reserved-timeslots/",
        views.UserReservedTimeSlotsList.as_view(),
        name="user-reserved-timeslots",
    ),
    path(
        "my-reserved-timeslots/past/",
        views.UserPastReservedTimeSlotsList.as_view(),
        name="user-reserved-timeslots-past",
    ),
    path(
        "clinic/<int:pk>/reserved-timeslots/",
        views.ClinicReservedTimeSlotsList.as_view(),
        name="clinic-reserved-timeslots",
    ),
    path(
        "clinic/<int:pk>/reserved-timeslots/past/",
        views.ClinicPastReservedTimeSlotsList.as_view(),
        name="clinic-reserved-timeslots-past",
    ),
    path(
        "api/v1/",
        include(
            [
                path("", views.api_root, name="api-home"),
                path("login/", user_views.login, name="api-login"),
                path(
                    "register/",
                    user_views.CreateUserView.as_view(),
                    name="api-register",
                ),
                path("clinics/", views.ClinicList.as_view(), name="clinic-list"),
                path(
                    "clinics/<int:pk>/",
                    views.ClinicDetail.as_view(),
                    name="clinic-detail",
                ),
                path("timeslots/", views.TimeSlotList.as_view(), name="timeslot-list"),
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
            ]
        ),
    ),
]
