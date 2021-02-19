from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice

# Create your views here.
def index(request):
    question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'q_list': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    context = {'selected_question': question}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])

    except(KeyError, Choice.DoesnotExist):
        return render(request, 'polls/detail.html', {
            'selected_question': question,
            'error_message': '아무것도 선택되지 않았습니다.'
        })
    else :
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)

