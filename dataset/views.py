# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


class views:
    TODO = HttpResponse("<h1>TODO</h1><h3>implement later</h3>")
    ERROR = HttpResponse("<h1>Error</h1><h3>implement later</h3>")
    html = ""
    def SHOW(self):
        return HttpResponse(self.html)

# Create your views here.
def close(request):
    return views.ERROR