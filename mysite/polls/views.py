from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.  How are you and how did you get to my wall? The other day i was wondering if this was live preview... Obviously not,")
