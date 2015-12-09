# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:27:08 2015

@author: emanuele
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)