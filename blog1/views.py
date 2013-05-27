from django.shortcuts import render_to_response
from forms import MsgForm
from models import Publication
from datetime import datetime
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

class AboutView(TemplateView):
    template_name = "about.html"

def blog_main(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                Publication (date=datetime.now(), text=cd['message']).save()
                form = MsgForm()
            except:
                form = MsgForm(request.POST)
                return render_to_response('blog.html', {'form': form, 'msg_list': Publication.objects.all(), 'db_error':True})
    else:
        form = MsgForm()
    return render_to_response('blog.html', {'form': form, 'msg_list': Publication.objects.all(), 'db_error':False})

class MsgListView(ListView):
    model = Publication
    template_name = "publication_list.html"

    def head(self, *args, **kwargs):
        last_msg = self.get_queryset().latest('date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_msg.date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response