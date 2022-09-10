from django.shortcuts import render
from apps.Profesores.models import Profesores
from django.db.models import Q

def Profesores_search(request):
   query = request.GET.get('q', '')
   #print("query: {}".format(query))
   results = (
       Q(nombre__icontains=query)
   )
   print("resuts: {}".format(results))
   data_context = Profesores.objects.filter(results).distinct()

   return render(request, 'profesores/templates/profesores/profesores_search.html', context={'data': data_context, "query": query})
