from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Action)
admin.site.register(Process)
admin.site.register(ProcessWay)
admin.site.register(Ticket)

