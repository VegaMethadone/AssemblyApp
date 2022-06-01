"""ipproger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [

    ###########################
    #### Лендинг проекта ######
    ###########################
    path('', views.index ),

    ###########################
    #### Макет под Jinja ######
    ###########################
    path('main', views.block),

    ###########################
    ### Центрыйльный раойн ####
    ###########################
    path('central_left', views.central_left),
    path('central_month', views.central_month),         
    path('central_plan', views.central_plan),     
    path('central_year', views.central_year),

    ###########################
    ## Адмиралтейский раойн ###
    ###########################
    path('admiralty_left', views.admiralty_left),
    path('admiralty_month', views.admiralty_month),         
    path('admiralty_plan', views.admiralty_plan),     
    path('admiralty_year', views.admiralty_year), 

    ###########################
    #### Выборгский раойн #####
    ###########################
    path('vyborgsky_left', views.vyborgsky_left),
    path('vyborgsky_month', views.vyborgsky_month),         
    path('vyborgsky_plan', views.vyborgsky_plan),     
    path('vyborgsky_year', views.vyborgsky_year),

    ###########################
    ### Калининский раойн #####
    ########################### 
    path('kalininsky_left', views.kalininsky_left),
    path('kalininsky_month', views.kalininsky_month),         
    path('kalininsky_plan', views.kalininsky_plan),     
    path('kalininsky_year', views.kalininsky_year),   

    ###########################
    ##### Кировский раойн #####
    ########################### 
    path('kirovsky_left', views.kirovsky_left),
    path('kirovsky_month', views.kirovsky_month),         
    path('kirovsky_plan', views.kirovsky_plan),     
    path('kirovsky_year', views.kirovsky_year),  

    ###########################
    ##### Колпинский раойн ####
    ###########################
    path('kolpinsky_left', views.kolpinsky_left),
    path('kolpinsky_month', views.kolpinsky_month),         
    path('kolpinsky_plan', views.kolpinsky_plan),     
    path('kolpinsky_year', views.kolpinsky_year), 

    ###########################
    # Красногвардейский раойн #
    ########################### 
    path('krasnogvardeysky_left', views.krasnogvardeysky_left),
    path('krasnogvardeysky_month', views.krasnogvardeysky_month),         
    path('krasnogvardeysky_plan', views.krasnogvardeysky_plan),     
    path('krasnogvardeysky_year', views.krasnogvardeysky_year),

    ###########################
    ##### Курортный раойн #####
    ########################### 
    path('resort_left', views.resort_left),
    path('resort_month', views.resort_month),         
    path('resort_plan', views.resort_plan),     
    path('resort_year', views.resort_year),

    ###########################
    ##### Московский раойн ####
    ########################### 
    path('moscowsky_left', views.moscowsky_left),
    path('moscowsky_month', views.moscowsky_month),         
    path('moscowsky_plan', views.moscowsky_plan),     
    path('moscowsky_year', views.moscowsky_year),

    ###########################
    ### Петроградский раойн ###
    ########################### 
    path('petrogradsky_left', views.petrogradsky_left),
    path('petrogradsky_month', views.petrogradsky_month),         
    path('petrogradsky_plan', views.petrogradsky_plan),     
    path('petrogradsky_year', views.petrogradsky_year),

    ###########################
    ##### Приморский раойн ####
    ########################### 
    path('primorsky_left', views.primorsky_left),
    path('primorsky_month', views.primorsky_month),         
    path('primorsky_plan', views.primorsky_plan),     
    path('primorsky_year', views.primorsky_year),

    ###########################
    #### Фрунзенский раойн ####
    ########################### 
    path('frunzensky_left', views.frunzensky_left),
    path('frunzensky_month', views.frunzensky_month),         
    path('frunzensky_plan', views.frunzensky_plan),     
    path('frunzensky_year', views.frunzensky_year),

    ###########################
    ######## СПБ Общее ########
    ########################### 
    path('saintP_general', views.saintP_general),
    path('saintP_left', views.saintP_left),         
    path('saintP_income', views.saintP_income),

    ###########################
    ##### Межрайонная  ########
    ########################### 
    path('interdistrict', views.interdistrict),      
]   


