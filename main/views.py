# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Category
from django.shortcuts import render_to_response

class IndexView(generic.ListView):
    model = Category
    template_name = 'main/index.html'
    context_object_name = 'all_categories'

class IndexViewEN(generic.ListView):
    model = Category
    template_name = 'main/indexEN.html'
    context_object_name = 'all_categories'

def google(request):
    return render_to_response('main/google3d8b31bd23ec2d59.html')


def robots(request):
    return render_to_response('main/Robots.txt')
