from django.views.generic import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from django.contrib.sites.models import get_current_site

class GnsLoginForm (FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'

    def SetRedirectFileName (self,new_redirect_field_name):
        self.redirect_field_name = new_redirect_field_name

    def get_context_data(self, **kwargs):
        context = {}
        if self.form: context['form'] = self.form
        if 'request' in kwargs:
            request = kwargs['request']
            redirect_to = request.REQUEST.get(self.redirect_field_name, '')
            context ['site'] = get_current_site(request)
            context ['site_name'] = context ['site'].name
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            context [self.redirect_field_name] = redirect_to,

        context.update(kwargs)
        return super(BlogMainView, self).get_context_data(**context)

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        request.session.set_test_cookie()
        context = self.get_context_data (request=request)
        return TemplateResponse(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        context = self.get_context_data (request=request)
        redirect_to = context [self.redirect_field_name]
        if form.is_valid():

            # Okay, security check complete. Log the user in.
            auth_login(request, self.form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)

        request.session.set_test_cookie()

        context = self.get_context_data (request=request)

        return TemplateResponse(request, self.template_name, context)



"""
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)
"""