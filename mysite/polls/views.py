from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Question

# Create your views here.


def hello(request):
    return HttpResponse("Hello,world.You're at the polls index.")

def hello_index1(request):
    return HttpResponse("Hello,world.You're at the polls index1 and using render.")
    #return render(request,"Hello,world.You're at the polls index1 and using render.")

#def detail(request,question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#def vote(request,question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', ',join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

#def index(requext):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context,request))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)




