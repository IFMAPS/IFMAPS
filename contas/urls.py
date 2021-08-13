from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/', views.SignUp.as_view(), name='cadastrar'),
]
