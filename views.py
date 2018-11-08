from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader


@csrf_exempt
def echo(request):

    par_name = ''
    par_value = ''
    statement = 'statement is empty'

    method = request.method
    if method == 'GET':
        if request.GET.get('a', ''):
            par_name = 'a:'
            par_value = request.GET['a']
        if request.GET.get('c', ''):
            par_name = 'c:'
            par_value = request.GET['c']

    if method == 'POST':
        if request.POST.get('b', ''):
            par_name = 'b:'
            print(request.POST['b'])
            par_value = request.POST['b']
        if request.POST.get('d', ''):
            par_name = 'd:'
            par_value = request.POST['d']

        if 'HTTP_X_PRINT_STATEMENT' in request.META:
            statement = 'statement is ' + request.META['HTTP_X_PRINT_STATEMENT']

    if par_name == '':
        method = ''
        par_name = ''
        par_value = ''

    template = loader.get_template('echo.html')

    context = {
        'method': method,
        'par_name': par_name,
        'par_value': par_value,
        'statement': statement,
    }

    return HttpResponse(template.render(context, request), status='200')


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
