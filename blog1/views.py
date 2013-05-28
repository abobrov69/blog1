from django.shortcuts import render_to_response, render
from forms import MsgForm
from models import Publication
from datetime import datetime
from django.views.generic import TemplateView, ListView, View, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class AboutView(TemplateView):
    template_name = "about.html"

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

class BlogMainView(ListView):
    form_class = MsgForm
    template_name = 'blog.html'
    context_object_name = 'msg_list'
    model = Publication
    show_msg_lenght = 60

    def get_queryset_with_cutted_txt (self):
        msg_lst = self.get_queryset ()
        if msg_lst:
            for msg in msg_lst:
                if len(msg.text) > self.show_msg_lenght: msg.text = msg.text[:self.show_msg_lenght-5] + ' ...'

        return msg_lst

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,  self.template_name, {'form': form, 'db_error':False, 'msg_list':  self.get_queryset_with_cutted_txt() }) #

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                Publication (date=datetime.now(), text=cd['message']).save()
                # form = MsgForm()
            except:
                form = self.form_class(request.POST)
                return render(request,  self.template_name, {'form': form, 'db_error':True, 'msg_list': self.get_queryset_with_cutted_txt()}) #
            return HttpResponseRedirect (reverse('blogclass'))
        return render(request, self.template_name, {'form': form})

class MsgListView(ListView):
    model = Publication
    template_name = "publication_list.html"
    context_object_name = 'messages_list'

    def head(self, *args, **kwargs):
        last_msg = self.get_queryset().latest('date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_msg.date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response