from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # method 1 **********************
    # template = loader.get_template('polls/index.html')
    # context = {'latest_question_list': latest_question_list, }
    # return HttpResponse(template.render(context, request))
    # end method 1 ******************

    # method 2 ***********************
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)
    # end method 2 ********************

    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello world. You are at the polls index")


def detail(request, question_id):
    # return HttpResponse("You are looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question,
                       'error_message': 'You did not select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

    # return HttpResponse("You are voting on question %s." % question_id)
