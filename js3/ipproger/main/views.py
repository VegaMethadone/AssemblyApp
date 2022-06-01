from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from django.http import JsonResponse
from .models import Articles, Articles_2

# Create your views here.
  

def index(request):
    return render(request, 'main/index.html')

def json(request):
    labels = []
    data = []

    queryset = Articles_2.objects.values('anons', 'numb')
    for entry in queryset:
        labels.append(entry['anons'])
        data.append(entry['numb'])

    return JsonResponse(data={
        'labels': labels,
        'data': data, 
    })


#time_published = Articles.objects.orver_by('time')


#def index(request):
#    kek = []
#    lol = []
#
#    news = Articles_2.objects.all()
#    for articles in news:
#        kek.append(articles.anons)
#        lol.append(articles.numb)
#    
#    return render(request, 'main/index.html', {
#        'labels': kek,
#       'data': lol,
#    })






