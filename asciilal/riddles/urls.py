from django.urls import path

from . import views

app_name = 'riddles'
urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.show, name='show'),
    path('<int:team_number>/submit/', views.submit, name='submit')
]