from django.shortcuts import render
from django.http import HttpResponse



###########################
#### Лендинг проекта ######
###########################
def index(request):
    return render(request, 'main/main page/index.html')

###########################
#### Макет под Jinja ######
###########################
def block(request):
    return render(request, 'main/nav bar/main.html')


###########################
### Центрыйльный раойн ####
###########################
def central_left(request):
    return render(request, 'main/nav bar/central_left.html' )

def central_month(request):
    return render(request, 'main/nav bar/central_month.html')

def central_plan(request):
    return render(request, 'main/nav bar/central_plan.html')

def central_year(request):
    return render(request, 'main/nav bar/central_year.html')


###########################
## Адмиралтейский раойн ###
###########################
def admiralty_left(request):
    return render(request, 'main/nav bar/admiralty_left.html' )

def admiralty_month(request):
    return render(request, 'main/nav bar/admiralty_month.html')

def admiralty_plan(request):
    return render(request, 'main/nav bar/admiralty_plan.html')

def admiralty_year(request):
    return render(request, 'main/nav bar/admiralty_year.html')

###########################
#### Выборгский раойн #####
###########################
def vyborgsky_left(request):
    return render(request, 'main/nav bar/vyborgsky_left.html' )

def vyborgsky_month(request):
    return render(request, 'main/nav bar/vyborgsky_month.html')

def vyborgsky_plan(request):
    return render(request, 'main/nav bar/vyborgsky_plan.html')

def vyborgsky_year(request):
    return render(request, 'main/nav bar/vyborgsky_year.html')


###########################
### Калининский раойн #####
###########################
def kalininsky_left(request):
    return render(request, 'main/nav bar/kalininsky_left.html' )

def kalininsky_month(request):
    return render(request, 'main/nav bar/kalininsky_month.html')

def kalininsky_plan(request):
    return render(request, 'main/nav bar/kalininsky_plan.html')

def kalininsky_year(request):
    return render(request, 'main/nav bar/kalininsky_year.html')


###########################
#### Кировский раойн ######
###########################
def kirovsky_left(request):
    return render(request, 'main/nav bar/kirovsky_left.html' )

def kirovsky_month(request):
    return render(request, 'main/nav bar/kirovsky_month.html')

def kirovsky_plan(request):
    return render(request, 'main/nav bar/kirovsky_plan.html')

def kirovsky_year(request):
    return render(request, 'main/nav bar/kirovsky_year.html')


###########################
#### Колпинский раойн #####
###########################
def kolpinsky_left(request):
    return render(request, 'main/nav bar/kolpinsky_left.html' )

def kolpinsky_month(request):
    return render(request, 'main/nav bar/kolpinsky_month.html')

def kolpinsky_plan(request):
    return render(request, 'main/nav bar/kolpinsky_plan.html')

def kolpinsky_year(request):
    return render(request, 'main/nav bar/kolpinsky_year.html')


###########################
# Красновгардейский раойн #
###########################
def krasnogvardeysky_left(request):
    return render(request, 'main/nav bar/krasnogvardeysky_left.html' )

def krasnogvardeysky_month(request):
    return render(request, 'main/nav bar/krasnogvardeysky_month.html')

def krasnogvardeysky_plan(request):
    return render(request, 'main/nav bar/krasnogvardeysky_plan.html')

def krasnogvardeysky_year(request):
    return render(request, 'main/nav bar/krasnogvardeysky_year.html')


###########################
#### Куротрный раойн #####
###########################
def resort_left(request):
    return render(request, 'main/nav bar/resort_left.html' )

def resort_month(request):
    return render(request, 'main/nav bar/resort_month.html')

def resort_plan(request):
    return render(request, 'main/nav bar/resort_plan.html')

def resort_year(request):
    return render(request, 'main/nav bar/resort_year.html')


###########################
#### Московский раойн #####
###########################
def moscowsky_left(request):
    return render(request, 'main/nav bar/moscowsky_left.html' )

def moscowsky_month(request):
    return render(request, 'main/nav bar/moscowsky_month.html')

def moscowsky_plan(request):
    return render(request, 'main/nav bar/moscowsky_plan.html')

def moscowsky_year(request):
    return render(request, 'main/nav bar/moscowsky_year.html')



###########################
### Петроградский раойн ###
###########################
def petrogradsky_left(request):
    return render(request, 'main/nav bar/petrogradsky_left.html' )

def petrogradsky_month(request):
    return render(request, 'main/nav bar/petrogradsky_month.html')

def petrogradsky_plan(request):
    return render(request, 'main/nav bar/petrogradsky_plan.html')

def petrogradsky_year(request):
    return render(request, 'main/nav bar/petrogradsky_year.html')



###########################
#### Приморский раойн #####
###########################
def primorsky_left(request):
    return render(request, 'main/nav bar/primorsky_left.html' )

def primorsky_month(request):
    return render(request, 'main/nav bar/primorsky_month.html')

def primorsky_plan(request):
    return render(request, 'main/nav bar/primorsky_plan.html')

def primorsky_year(request):
    return render(request, 'main/nav bar/primorsky_year.html')


###########################
#### Фрунзенский раойн ####
###########################
def frunzensky_left(request):
    return render(request, 'main/nav bar/frunzensky_left.html' )

def frunzensky_month(request):
    return render(request, 'main/nav bar/frunzensky_month.html')

def frunzensky_plan(request):
    return render(request, 'main/nav bar/frunzensky_plan.html')

def frunzensky_year(request):
    return render(request, 'main/nav bar/frunzensky_year.html')


###########################
######## СПБ Общее ########
########################### 
def saintP_general(request):
    return render(request, 'main/nav bar/saintP_general.html' )

def saintP_left(request):
    return render(request, 'main/nav bar/saintP_left.html')

def saintP_income(request):
    return render(request, 'main/nav bar/saintP_income.html')


###########################
##### Межрайонная  ########
###########################
def interdistrict(request):
    return render(request, 'main/nav bar/interdistrict.html' ) 



