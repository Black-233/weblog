from django.contrib import admin
from .models import Entry, Topic, Tag
# Register your models here.

admin.site.register(Entry)
admin.site.register(Topic)
admin.site.register(Tag)