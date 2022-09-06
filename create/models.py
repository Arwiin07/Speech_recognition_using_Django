from django.db import models

# Create your models here.
class Person(models.Model):
    file_name=models.CharField(max_length=20)
    transcripted_sentence=models.TextField()
    Sentiment_analysis=models.TextField()
    transcripted_Sentence_slice=models.TextField()

    def __str__(self):
        return self.file_name
