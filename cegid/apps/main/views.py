from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Count
from django.template import RequestContext
from django.shortcuts import render, render_to_response
import hashlib

def index_view(request):
    context = {'active':'home'}
    return render(request, 'main/index.html', context)

def signup_view(request):
    context = {'active':'home'}
    return render(request, 'main/signup.html', context)

def about_view(request):
    context = {'active':'home'}
    return render(request, 'main/about.html', context)

def search_view(request):
    return render(request, 'main/search.html')

# Error Pages ##################################################################

def handler404(request):
    response = render_to_response('main/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('main/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
