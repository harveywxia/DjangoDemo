from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.forms import StudentForm, QuestionForm
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


def algorithm(request):
    alg_name = request.GET.get('p1')
    para1 = request.GET.get('p2')
    return HttpResponse("Algorithm:{0} with parameter: {1} is running.".format(alg_name, para1))


def algorithm2(request, alg_name, para1):
    return HttpResponse("Algorithm:{0} with parameter: {1} is running.".format(alg_name, para1))


def login(request):
    return render(request, 'polls/login.html')


# 以post方式获取表单数据
def loginresult(request):
    username = request.POST.get('user_name')
    password = request.POST.get('password')
    if username == "admin" and password == "123":
        return HttpResponseRedirect(redirect_to='/polls')
    else:
        return HttpResponse("username:{0}. password:{1}".format(username, password))


def get_student(request):
    if request.method == 'GET':
        # form = StudentForm(request.POST)
        # 为form添加默认数据。
        default_data = {'question_text': 'Default question.', 'pub_date': timezone.now()}
        form = QuestionForm(data=default_data)
        print(form)
        if form.is_valid():
            pass

    else:
        form = QuestionForm()
    return render(request, 'polls/student.html', {'form': form})


def nameinfo(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        sex = form.cleaned_data['sex']
        age = form.cleaned_data['age']
        return HttpResponse("name:{0},sex:{1},age{2}".format(name, sex, age))
    else:
        return HttpResponse("form wrong!!!")
