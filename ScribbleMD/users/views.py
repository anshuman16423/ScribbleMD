from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import RegisterUser,login_main
from . import models


def index(request):
    # To be Continued

    if request.method == 'POST':

        form = login_main(request.POST)
        if form.is_valid():
            l = models.User.objects.all()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            f = 0
            for user in l:

                if user.username == username and user.password == password:
                    f = 1
                    print username
                    break
            if f:
                request.session['username'] = user.username

            request.session['flag'] = f

        return HttpResponseRedirect('users')
    if 'username' in request.session:
        if 'flag' in request.session:
            request.session.pop('flag')
        if 'flag1' in request.session:
            request.session.pop('flag1')
        return HttpResponseRedirect('./')
    flag = ''
    if 'flag' in request.session:
        if request.session['flag'] == 0:
            flag = "Wrong Credentials"
    form = login_main()
    temp = loader.get_template('users/login_main.html')
    context = {'form': form, 'prev': flag}
    return HttpResponse(temp.render(context, request))


def signup(request):
    if 'username' in request.session:
        return HttpResponse("<h3>You're already logged In")
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid() and form.cleaned_data['username'] not in [i.username for i in models.User.objects.all()]:
            if 'flag1' in request.session:
                request.session.pop('flag1')
            a = models.User()
            a.username = form.cleaned_data['username']
            a.password = form.cleaned_data['password']
            a.email = form.cleaned_data['email']
            a.save()
            """
            form = login_main()
            temp = loader.get_template('users/login_main.html')"""
            return HttpResponseRedirect('../users')
        else:
            request.session['flag1'] = 1

    str1 = ''
    if 'flag1' in request.session:
        str1 = 'Something Went Wrong!! Please Try Again'
    form = RegisterUser()

    all_model = models.User.objects.all()
    temp = loader.get_template('users/index.html')
    context = {'all_user': all_model, 'form': form, 'str': str1}
    return HttpResponse(temp.render(context, request))



def logout(request):
    try:
        a = request.session.pop('username')
        return HttpResponseRedirect('../users')
    except:
        print 'error'
        return HttpResponseRedirect('../users')
