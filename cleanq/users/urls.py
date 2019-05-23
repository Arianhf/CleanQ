from django.urls import include, path
from users.views import user, basic, rep


from . import views

urlpatterns = [
    path("", views.user.UserListView.as_view(), name="user-list"),
    path("<int:pk>/", views.user.UserDetailView.as_view(), name="user-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", user.SignUpView.as_view(), name="signup"),
    path("accounts/signup/rep/", rep.RepSignUpView.as_view(), name="rep_signup"),
    path(
        "accounts/signup/basic/", basic.BasicSignUpView.as_view(), name="basic_signup"
    ),
]
