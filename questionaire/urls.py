# This file defines list of all the URL's exposed to the client

from django.urls import path
from . import views


urlpatterns = [
    # Web Page URL's
    path('', views.home), 
    path('food/', views.food),
    path('travel/', views.travel),
    path('pro/', views.pro),

    # URL's for different questionnaire
    path('QuestionnairFood/', views.food_question),
    path('QuestionnairTravel/', views.travel_question),
    path('QuestionnairPro/', views.pro_question)
]
