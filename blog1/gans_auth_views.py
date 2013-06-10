from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from django.contrib.sites.models import get_current_site
from functools import wraps
from django.utils.decorators import available_attrs

def gns_login_required(login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            request.session ['request_POST'] = request.POST
            a = request.session
            bbb = asdasdasd
            if is_authenticated(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            # urlparse chokes on lazy objects in Python 3, force to str
            resolved_login_url = force_str(
                resolve_url(login_url or settings.LOGIN_URL))

            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
#            ddkj = asdhhkjafakjh
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator


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

            context [self.redirect_field_name] = redirect_to
        context.update(kwargs)
        return super(GnsLoginForm, self).get_context_data(**context)

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        request.session.set_test_cookie()
        context = self.get_context_data (request=request)
        return TemplateResponse(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        self.form = self.form_class(data=request.POST)
        context = self.get_context_data (request=request)
        redirect_to = context [self.redirect_field_name]
        q1 = request.session ['request_POST']
        if self.form.is_valid():

            # Okay, security check complete. Log the user in.
            auth_login(request, self.form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

#            request.session ['test1'] = 'test2'
            q2 = request.session ['request_POST']
            aaa = ddd
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
