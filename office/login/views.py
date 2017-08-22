from django.contrib.auth import authenticate,login,logout

@csrf_exempt
def user_login(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('next', '/') or '/')

    return render_to_response("xxxx/login.html", locals(), RequestContext(request))