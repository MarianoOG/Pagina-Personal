# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, Experience, Skill

# Register your models here.
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Experience)
