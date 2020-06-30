from django.contrib import admin
from django.urls import path
from voteapp import views

# app_name='polls'
urlpatterns = [
    path('home/',views.HomeView),
    path('question/',views.QuestionView,name='question'),
    path('<int:id>/',views.QuestionDetailView,name='detail_question'),
    path('<int:id>/vote/',views.VoteView,name='vote'),
    path('<int:id>/results/',views.resultsView,name='results'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),


]
