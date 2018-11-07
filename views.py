from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def simple_route(request):
    if request.method == 'GET':
        return HttpResponse('')
    elif request.method == 'POST' or request.method == 'PUT':
        return HttpResponse('POST', status='405')


@csrf_exempt
def slug_route(request, slug):
    return HttpResponse(slug)


@csrf_exempt
def sum_route(request , digit1, digit2):
    return HttpResponse(int(digit1) + int(digit2))


@csrf_exempt
def sum_get_method(request):
    if request.method == 'POST':
        return HttpResponse('', status='405')
    else:
        a = request.GET.get('a', '')
        b = request.GET.get('b', '')

        try:
            a, b = int(a), int(b)
        except:
            return HttpResponse('', status='400')

        return HttpResponse(a+b)


@csrf_exempt
def sum_post_method(request):
    if request.method == 'GET':
        return HttpResponse('', status='405')
    else:
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')

        try:
            a, b = int(a), int(b)
        except:
            return HttpResponse('', status='400')

        return HttpResponse(a+b)

