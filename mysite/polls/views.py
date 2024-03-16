from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # SHORTER METHOD
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

    # LONG METHOD
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list
    # }
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # LONG METHOD
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # SHORTER METHOD
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")