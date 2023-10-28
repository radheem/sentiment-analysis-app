from django.test import TestCase
from classification_app.models import UserClassifications
from classification_app.roberta_base_app import sentimentAnalysis
from dotenv import load_dotenv

import os 
load_dotenv()


class ClassificationAppModelTestCase(TestCase):
    def setUp(self) -> None:
        obj = UserClassifications.objects.create(
            user_id = 1,
            user_name = "test",
            input_text = "test",
            sentiment = "positive"
        )
        return 
    
    def test_user_classifications_model(self):
        obj = UserClassifications.objects.get(user_id=1)
        self.assertEqual(obj.user_id,1)
        self.assertEqual(obj.user_name,"test")
        self.assertEqual(obj.input_text,"test")
        self.assertEqual(obj.sentiment,"positive")
        return
    
class ClassificationAppClassifierTestCase(TestCase):
    def setUp(self) -> None:
        model_name  = str(os.getenv('SENTIMENT_MODEL_NAME'))
        model_path = str(os.getenv('SENTIMENT_MODEL_PATH'))
        self.classification_model = sentimentAnalysis(model_name,model_path,True) 
        return 
    
    def test_sentiment_classifier(self):
        sentiment = self.classification_model.get_sentiment("I am happy")
        self.assertEqual(sentiment,"positive")
        sentiment = self.classification_model.get_sentiment("I am sad")
        self.assertEqual(sentiment,"negative")
        return