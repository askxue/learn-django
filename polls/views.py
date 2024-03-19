from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


# 视图层，类似于Java web 里的controller

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list, }
    return render(request, "polls/index.html", context)


# 投票详情
def detail(request, question_id):
    # 如果不存在则抛出404异常
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


# 投票结果
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# 给问题投票
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
