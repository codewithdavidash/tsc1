from django.contrib import admin
from .models import (
    HTML_CSS,
    JavaScript,
    Python
)


admin.site.register([
    HTML_CSS,
    JavaScript,
    Python
])
