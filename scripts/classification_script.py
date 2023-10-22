import sys
from pathlib import Path
import os 
curr_dir = Path(__file__).parent.parent.absolute()
sys.path.append(os.path.join(curr_dir,'classification_app'))

from roberta_base_app import sentimentAnalysis
from models import SentimentChoices

def main():
    model_name = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
    model_path = os.path.join(curr_dir,'classification_app/trained_model', 'roberta_base_sentiment_001')
    classification_model = sentimentAnalysis(model_name,model_path,True)
    text = "I am so happy"
    sentiment = classification_model.get_sentiment(text)
    # print("sentiment: ",sentiment)
    print("sentiment: ",SentimentChoices[sentiment])



if __name__ == '__main__':
    main()