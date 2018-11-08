from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.urls import path

urlpatterns=[

      path('',views.index,name="index"),
      #127.0..0.1/polls/
      path('<int:question_id>/',views.detail,name="detail"),
      path('<int:question_id>/results',views.results,name="results"),
      path('<int:question_id>/vote',views.vote,name="vote"),
]