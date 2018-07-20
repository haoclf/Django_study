from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('',views.index,name='index'),
    # /polls/index1
    path('index1',views.hello_index1,name='index1'),
    # /polls/5/
    path('<int:question_id>',views.detail,name='detail'),
    #/polls/5/results
    path('<int:question_id>/results',views.results,name='results'),
    #/polls/5/vote
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
