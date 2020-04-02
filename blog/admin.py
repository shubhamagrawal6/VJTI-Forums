from django.contrib import admin
from .models import Post, Comment

admin.site.site_header='VJTI Forum Administration'
admin.site.register(Post)
admin.site.register(Comment)