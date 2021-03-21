
from django.contrib import admin
from django.urls import path
from .views import home , login , signup , add_todo , signout , delete_todo, change_todo
from .views import tododetails


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ),
   path('tododetails/<str:details>', tododetails),
   path('logout/' , signout ), 
]
