from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'q_list': question_list} # 일반적으로 context라는 이름을 쓰긴 하지만 아무거나 써도 된다
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 숫자 하나가 question_id 로 들어옴 => 설문에 대한 PK
    question = get_object_or_404(Question, pk=question_id)
    aa = {'selected_question' : question}
    return render(request, 'polls/detail.html', aa)

def vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
    except(KeyError, Choice.DoesNotExist) :
        # PK가 없어서 에러가 날 경우
        return render(request, 'polls/detail.html', {
            'selected_question': question,
            'error_message': '아무것도 선택하지 않았어요!'
        })
    else :
        selected_choice.votes += 1
        selected_choice.save()
        # client에게 다시 요청하라고 url을 보내줌/ reverse : url.py(URLConf에 있는 name을 이용해서 url형식으로 변환
        return HttpResponseRedirect(reverse('polls:results', 
                                            args=(question.id,))) # result를 url로 변환 / () : tuple 형태

        # context = {'selected_question': question}
        # return render(request, 'polls/detail.html', context)


def results (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{
        'question': question
    })