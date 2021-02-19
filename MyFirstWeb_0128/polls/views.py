from django.shortcuts import render
from polls.models import Question

# Create your views here.
def index(request):
    # 데이터베이스를 뒤져서 설문목록을 가져옴
    # (테이블명 : polls_question, 클래스명 : Question)
    question_list = Question.objects.all().order_by('-pub_date')[0:5]  # order_by : 정렬 (꼭 필요한건 아님) / '-' : 내림차순
    # 데이터 전달용 dictionary를 만들어요
    context = {'q_list': question_list}
    return render(request, 'index.html', context)



