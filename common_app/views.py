from django.shortcuts import render


# Create your views here.
def articles_list(request):
    return render(request, 'common_app/index.html', {})
