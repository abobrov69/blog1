from django.shortcuts import render_to_response
from forms import MsgForm
from models import Blog1
from datetime import datetime

def blog_main(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                Blog1 (publication_date=datetime.now(), publication_text=cd['message']).save()
                form = MsgForm()
            except:
                form = MsgForm(request.POST)
                return render_to_response('blog.html', {'form': form, 'msg_list': Blog1.objects.all(), 'db_error':True})
    else:
        form = MsgForm()
    return render_to_response('blog.html', {'form': form, 'msg_list': Blog1.objects.all(), 'db_error':False})

