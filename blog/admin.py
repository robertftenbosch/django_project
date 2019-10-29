from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Post
# Register your models here.
admin.site.register(Post)