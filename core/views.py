from django.shortcuts import render
from .forms import Form
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import UserInfo
from .render import Render
from django.views.generic import View
from threading import Thread, activeCount

# Create your views here.
def FormView(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/result/')
    else:
        form = Form()
        return render(request, 'core/base.html', {
            'form':form,
        })

def FormData(request):
    context ={}
    return render(request,'core/result.html',context)

class Pdf(View):
    def get(self, request):
        info = UserInfo.objects.all().order_by('-id')[:1]
        params = {
            'info': info,
            'request': request
        }
        return Render.render('core/pdf_temp.html', params)



