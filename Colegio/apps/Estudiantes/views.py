from django.shortcuts import render

# Create your views here.

def Colegio_list(request):

    return render(request, 'Colegio/Colegio_list.html', {})
