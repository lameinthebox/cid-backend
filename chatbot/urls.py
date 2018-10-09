from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from chatbot import views


urlpatterns = [
    path('auth/signup/', views.signup),
    path('auth/signin/', views.signin),
    path('auth/signout/', views.signout),
    path('auth/withdraw/', views.withdraw),
    path('users/', views.MuserList.as_view()),
    path('users/<int:pk>/', views.MuserDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)