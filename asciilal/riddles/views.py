from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice, Team
from .forms import TeamSelectionForm


def index(request):
    teamForm = TeamSelectionForm()
    context = {'form': teamForm}
    return render(request, 'riddles/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'riddles/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'riddles/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'riddles/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('riddles:results', args=(question.id,)))

def show(request):
    try:
        team = Team.objects.get(pk=request.GET['teamNum'])
    except (KeyError, Team.DoesNotExist):
        teamForm = TeamSelectionForm()
        return render(request, 'riddles/index.html', {
            'form': teamForm,
            'error_message': "You didn't enter a valid team number.",
        })
    else:
        return render(request, 'riddles/show.html', {'team': team.team_number})
