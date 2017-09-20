from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, Justin.  Way to request that web page.")
