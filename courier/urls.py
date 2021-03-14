from django.urls import path 
from courier import views 

urlpatterns = [ 
    path('', views.courier, name='courier'),
]