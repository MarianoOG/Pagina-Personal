# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    nameEN = models.CharField(max_length=25, default='')

    def order_by_rank(self):
        return self.skill_set.order_by('rank').reverse()

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rank = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def one(self):
        return self.rank >= 1

    def two(self):
        return self.rank >= 2

    def three(self):
        return self.rank >= 3

    def four(self):
        return self.rank >= 4

    def five(self):
        return self.rank >= 5

    def __str__(self):
        return self.name


class Experience(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nameEN = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    descriptionEN = models.CharField(max_length=200)
    coverImageURL = models.CharField(max_length=150)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.name
