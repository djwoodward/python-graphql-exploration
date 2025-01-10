from django.http import HttpResponse

def app_world(request):
    return HttpResponse("app, World!")