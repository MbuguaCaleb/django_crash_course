from django.shortcuts import render

# Controllers


def index(request):
    return render(request, 'pages/index.html')
