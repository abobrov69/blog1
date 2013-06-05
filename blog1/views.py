#from django.shortcuts import render_to_response, render
from sys import exc_info
from forms import MsgForm, MsgForm2
from models import Publication
from datetime import datetime
from django.views.generic import TemplateView, ListView # , View, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django.contrib.auth.models import AnonymousUser
from django.views.generic.detail import DetailView


class AboutView(TemplateView):
    template_name = "about.html"

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

"""
def blog_main(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                Publication (date=datetime.now(), text=cd['message']).save()
                # form = MsgForm()
            except:
                form = MsgForm(request.POST)
                return render_to_response('blog.html', {'form': form, 'msg_list': Publication.objects.all(), 'db_error':True})
            return HttpResponseRedirect (reverse('blogmain'))
    else:
        form = MsgForm()
    return render_to_response('blog.html', {'form': form, 'msg_list': Publication.objects.all(), 'db_error':False})
"""
class MsgListView(ListView):
    model = Publication
    template_name = "publication_list.html"
    context_object_name = 'messages_list'

class BlogMainView(MsgListView):
    form_class = MsgForm
    context_object_name = 'msg_list'
    show_msg_lenght = 60
    paginate_by = 5
    db_error = False
    form = False
    template_name = 'blog.html'


    def get_template_names(self):
        return [self.template_name]

    def get_queryset (self):
        msg_lst = super(BlogMainView,self).get_queryset ()
        if msg_lst:
#            msg_lst = [msg.text = msg.text[:self.show_msg_lenght-5] + ' ...' if len(msg.text) > self.show_msg_lenght for msg in msg_lst]
            for msg in msg_lst:
                if len(msg.text) > self.show_msg_lenght: msg.text = msg.text[:self.show_msg_lenght-5] + ' ...'
        return msg_lst

#    def render_to_response(self, context, **response_kwargs):
#        a = dc
#        return super (BlogMainView,self).render_to_response(self, context, **response_kwargs)


    def get_context_data(self, **kwargs):
        context = {'db_error': self.db_error}
        if self.form: context['form'] = self.form
        context.update(kwargs)
        return super(BlogMainView, self).get_context_data(**context)

    def SetFormUser (self,request):
        self.form.user = '' if request.user.is_anonymous() else request.user.username
#        u = self.form.user
#        asdqd = asdasdasdsd

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        self.SetFormUser (request)
#        aaaa = ldfkldfk
        return super(BlogMainView, self).get (request)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        self.SetFormUser (request)
#        context = {'form': self.form}
#        ib = self.form.is_bound
#           aaaaaaaaaa = ffffffffff
        if self.form.is_valid():
            cd = self.form.cleaned_data
            self.db_error = False
            try:
                Publication (date=datetime.now(), text=cd['message'], author=request.user).save()
                # form = MsgForm()
            except DatabaseError:
                self.form = self.form_class(request.POST)
                self.db_error = exc_info()[1].message
                return super(BlogMainView, self).get (request)  #  self.render_to_response(self.get_context_data(context)) #
            return HttpResponseRedirect (reverse('blogclass'))
        return super(BlogMainView, self).get (request)  #  self.render_to_response(self.get_context_data(context))

class MsgCreate(CreateView):
    form_class = MsgForm2
    model = Publication
    template_name = "publication_form.html"
    # context_object_name = 'messages_list'

    def form_valid(self, form):
        form.instance.date=datetime.now()
        return super(MsgCreate, self).form_valid(form)

class MsgUpdate(UpdateView):
    form_class = MsgForm2
    model = Publication
    success_url = reverse_lazy('blogclass')
    template_name = "publication_form.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.username <> self.get_object().author.username:
            self.template_name = "publication_user_error.html"
        return super(MsgUpdate, self).dispatch(request, *args, **kwargs)

class MsgDelete(DeleteView):
    model = Publication
    success_url = reverse_lazy('blogclass')
    template_name = "publication_confirm_delete.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.username <> self.get_object().author.username:
            self.template_name = "publication_user_error.html"
        return super(MsgDelete, self).dispatch(request, *args, **kwargs)

class MsgView (DetailView):
      model = Publication
      template_name = "publication_detail.html"