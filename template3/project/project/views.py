from django.http import HttpResponse
from django.core.cache import cache

import datetime


def index(request):
    now = datetime.datetime.now()

    cache.get_or_set("counter", 0)
    counter = cache.incr("counter")

    html = """
    <html>
    <body>
    <p>It is now %s.</p>
    <p>Counter %s.</p>
    <p>User: %s.</p>
    </body>
    </html>
    """ % (
        now, counter, request.user
    )
    return HttpResponse(html)
