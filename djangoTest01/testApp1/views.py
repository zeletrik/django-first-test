from django.http import HttpResponse


def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def goodMorning(request, name):
    text = "<h1>Good Morning %s </h1>" % name
    return HttpResponse(text)
