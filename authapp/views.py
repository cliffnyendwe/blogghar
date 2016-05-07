from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def user_profile(request, username):
    # getting default user model
    UserModel = get_user_model()
    profile = get_object_or_404(
        UserModel.objects.select_related(), username=username
    ).profile
    return render(request, 'authapp/user_profile.html', {'profile': profile})


@login_required
def profile_redirector(request):
    return redirect('profile', username=request.user.username)
