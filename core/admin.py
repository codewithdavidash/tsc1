from django.contrib import admin
from .models import HTML, JS, PYTHON, Comment, Assignments

# Register your models here.
admin.site.register(HTML)
admin.site.register(JS)
admin.site.register(PYTHON)
admin.site.register(Comment)
admin.site.register(Assignments)
