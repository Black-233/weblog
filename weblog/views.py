from django.shortcuts import render
from .models import Entry, Topic, Tag
import datetime
# Create your views here.
def index(request):
	entrys = Entry.objects.all()
	context = {"now_year": "{}".format(datetime.date.today().year), "entrys_list": entrys}
	return render(request, 'weblog/index.html', context)