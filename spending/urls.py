from django.urls import path
from spending.views import Signupview,GetMeView,ExpenseListCreateView

urlpatterns = [
    path("register/",Signupview.as_view()),

    path("me/",GetMeView.as_view()),
    path('expense/',ExpenseListCreateView.as_view()),
    
]