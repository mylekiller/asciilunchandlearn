from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Team(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    team_number = models.IntegerField(default=0)
    correct_date = models.DateTimeField('Date Answered Correct', default=None, blank=True, null=True)
