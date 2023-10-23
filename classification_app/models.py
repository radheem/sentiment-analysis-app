from django.db import models
from enum import Enum

class SentimentChoices(Enum):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'

class UserClassifications(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_name = models.TextField()
    input_text = models.TextField()
    createdAt= models.DateTimeField(auto_now=True)
    updatedAt=models.DateTimeField(auto_now=True)
    sentiment = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.value) for tag in SentimentChoices],
        default=SentimentChoices.NEUTRAL.value,
    )
    class Meta:
        db_table = "UserClassificationRecord"
        managed=True
        index_together=[
            ("user_id","createdAt")
        ]