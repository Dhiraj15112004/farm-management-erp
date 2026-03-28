from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def role_required(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_role = getattr(request.user, 'role', None)

            if user_role in allowed_roles:
                return view_func(request, *args, **kwargs)

            return redirect('role_redirect')
        return wrapper
    return decorator