from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'exam'

    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    question = models.CharField(max_length=512)
    answer1 = models.CharField(max_length=512)
    answer2 = models.CharField(max_length=512)
    answer3 = models.CharField(max_length=512)
    correct_ans = models.CharField(max_length=512)
    exam_detail = models.ForeignKey(Exam, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'quiz'
        
    # def __str__(self):
    #     return self.question
        
        
class User(models.Model):
    email = models.CharField(max_length=512)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    
    class Meta:
        db_table = 'user'
