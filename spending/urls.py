from django.urls import path
from spending.views import Signupview,GetMeView,ExpenseListCreateView,ExpenseRetrieveUpdateDeleteView

urlpatterns = [
    path("register/",Signupview.as_view()),

    path("me/",GetMeView.as_view()),
    path('expense/',ExpenseListCreateView.as_view()),
    path('expense/<int:pk>/',ExpenseRetrieveUpdateDeleteView.as_view()),
    
    
]