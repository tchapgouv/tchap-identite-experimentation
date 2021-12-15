#from urllib.parse import urlparse, urlunparse
#
#from django.conf import settings
#
##from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model, login as auth_login
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.sites.shortcuts import get_current_site
#from django.utils.decorators import method_decorator
#from django.views.decorators.cache import never_cache
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponseRedirect
#from django.utils.http import (
#    url_has_allowed_host_and_scheme, urlsafe_base64_decode,
#)
#
#from django.shortcuts import resolve_url
#from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.core.cache import cache

UserModel = get_user_model()

@login_required
def profile(request):
    #user = cache.get(request.username)
    #return HttpResponse(user)
    user = cache.get(request.user)
    text = '''
        Vous êtes connecté en tant que :<br/>
        Email : {email}<br/>
        Matrix ID : {matrix_id}<br/>
    '''.format(email=user.email, matrix_id=user.matrix_user_id)
    return HttpResponse(text)

class MatrixLoginView(LoginView):

    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user(), backend='matrix_connect.backends.MatrixBackend')
        return HttpResponseRedirect(self.get_success_url())