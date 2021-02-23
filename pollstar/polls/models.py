from django.db import models

# Models interact with my database table
# We create our database models
# Create your models here.


# All classes extend the base model
# An id is created automatically which is our pimary key and which auto increments
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # When i delete a question all related choices will be deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
