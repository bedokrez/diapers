# Create your views here.
# Create your views here.
#remember template variables require an underscore
from django.template.loader import get_template
from django.shortcuts import render_to_response
#from django.template import Context
#from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    t = get_template('test.html')
    message = "Hello, world. You're at the poll index."
    number = 25
#    html = t.render(Context({'current_date': message}))
#    return HttpResponse(html)
    return render_to_response('test.html', {'current_date': message})