from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def root_user_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not hasattr(request.user, 'userprofile') or not request.user.userprofile.is_root_user:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper