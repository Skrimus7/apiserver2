from django.http import HttpResponse
from django.shortcuts import render


def search_form(request):
    return render(request, 'search_form.html')


def products(request, uuid):
    type = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(uuid, type)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


###def search(request):
###    if 'q' in request.GET:
###       message = 'You searched for: %r' % request.GET['q']
###    else:
###        message = 'You submitted an empty form.'
###    return HttpResponse(message)###