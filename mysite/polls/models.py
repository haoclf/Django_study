from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)   #字符类型,CharField
    pub_date = models.DateTimeField('date published')   #时间类型,DateTimeField
    def __str__(self):
        return self.question_text

class Choise(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

