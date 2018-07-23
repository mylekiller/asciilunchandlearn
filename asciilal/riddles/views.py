from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from datetime import datetime
import re

from .models import Question, Team
from .forms import TeamSelectionForm, RiddleSubmissionForm


def index(request):
    teamForm = TeamSelectionForm()
    context = {'form': teamForm}
    return render(request, 'riddles/index.html', context)

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
        form = RiddleSubmissionForm()
        return render(request, 'riddles/show.html', {'team_num': team.team_number, 'question': team.question, 'form': form})

def submit(request, team_number):
    team = get_object_or_404(Team, pk=team_number)
    question = team.question
    if (question.answer == decode_string(request.GET.get('submission', ''))):
        return render(request, 'riddles/success.html', {'success': "true", 'team': team_number, 'timestamp': datetime.now().strftime("%m-%d-%Y %H:%M:%S")})
    else:
        form = RiddleSubmissionForm()
        return render(request, 'riddles/show.html', {'team_num': team.team_number, 'question': question, 'form': form, 'error_message': "Incorrect Answer Try Again!"})


def decode_string(answer):
    b = re.sub(r"[\D2-9]*", "", answer)
    return bytes([int(b[i:i+8], 2) for i in range(0, len(b), 8)]).decode().strip()


