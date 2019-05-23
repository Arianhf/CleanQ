from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def rep_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    """
    Decorator for views that checks that the logged in user is a rep,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_rep,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def basic_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    """
    Decorator for views that checks that the logged in user is a basic user,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_basic,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
