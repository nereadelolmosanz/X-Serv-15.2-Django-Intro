from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_main(request):
    header = '<h1>My Application</h1>'
    options = '<p>Optional Resources: /hello, /bye, /num.</p>'
    response = header + options
    return HttpResponse(response)

def say_hello(request, name):
    if name == "":
        response = '<h3>Hello!</h3><p>You can type your name like this: '
        response += '"http://localhost:1234/hello/YourName".</p>'
    else:
        response = ('Welcome, %s' % name, '!')
    return HttpResponse(response)

def say_bye_to(request, name):
    if name == "":
        response = '<h3>ByeBye</h3> <p>You can type your name like this: '
        response += '"http://localhost:1234/bye/YourName".</p>'
    else:
        response = ('Bye, %s' % name, '!')
    return HttpResponse(response)

def say_num(request, num):
    if num == "":
        response = '<h3>Error!</h3> <p>Type any number like this: '
        response += '"http://localhost:1234/number/YourNumber".</p>'
    else:
        response = ('The number is: %s' % num)
    return HttpResponse(response)


def resourceError(request):
    message = ('Resource not available.')
    options = '<p>Optional Resources: /hello, /bye, /num.</p>'
    response = message + options
    return HttpResponse(response)
