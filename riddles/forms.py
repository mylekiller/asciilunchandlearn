from django import forms

class TeamSelectionForm(forms.Form):
    teamNum = forms.IntegerField(label="Team Number", max_value=7, min_value=1)

class RiddleSubmissionForm(forms.Form):
	submission = forms.CharField(label="Answer")