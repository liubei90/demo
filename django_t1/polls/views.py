# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

# def index(request):
#     last_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': last_question_list,
#     }

#     return HttpResponse(template.render(context, request))

refresh_count = 0

class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
    # context_object_name = 'the_latest_question_list'

    # def get_queryset(self):
    #     return Question.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global refresh_count
        refresh_count += 1

        context['refresh_count'] = str(refresh_count)
        context['the_latest_question_list'] = Question.objects.order_by('-pub_date')[:5]

        return context


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         template = loader.get_template('polls/detail.html')
#         context = {
#             'question': question,
#         }

#         return HttpResponse(template.render(context, request))
#     except Question.DoesNotExist:
#         raise Http404(f'question:{question_id} does not exists!')

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


# def results(request, question_id):
#     pass


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_and_add_refresh_count(request):
    import json

    global refresh_count
    refresh_count += 1

    res = HttpResponse()
    res['Content-Type'] = 'application/json;charset=utf-8'
    res.content = json.dumps({ 'refresh_count': refresh_count }).encode(encoding='utf8')

    return res
