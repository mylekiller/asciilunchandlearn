from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Team(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    team_number = models.IntegerField(default=0)
    correct_date = models.DateTimeField('Date Answered Correct', default=None, blank=True, null=True)

    def __str__(self):
        return str(self.team_number)
