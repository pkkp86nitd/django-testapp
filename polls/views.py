from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from polls.models import Question,Choice
from django.template import loader,RequestContext
from django.template.response  import TemplateResponse 
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    latest_questions= Question.objects.order_by('pub_date')[:5]
   # output=",".join(q.question_text for q in latest_questions)
    context={'latest_questions':latest_questions}
    return render(request,'polls/index.html',context) 

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
     

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

