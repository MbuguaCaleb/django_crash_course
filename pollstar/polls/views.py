# Are like controllers in Laravel(Django is MVT)
# Create your views here.
# Render templates or  return JSON
from django.shortcuts import render

from .models import Question, Choice


# Get Questions and display them
def index(request):
    # -ve means i am ordering in descending  //:5 is the limit of Questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# Show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get Question and display results


# Get question and display results
def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
