import sys
from pathlib import Path
import os 
curr_dir = Path(__file__).parent.parent.absolute()
sys.path.append(os.path.join(curr_dir,'classification_app'))

from roberta_base_app import sentimentAnalysis
from models import SentimentChoices

def main():
    # add trained models folder to gitignore
    model_path = os.path.join(curr_dir,'path/to/model', 'name_of_model')
    model_name = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
    classification_model = sentimentAnalysis(model_name,"",True)
    text = "I am so happy"
    sentiment = classification_model.get_sentiment(text)
    print("sentiment: ",SentimentChoices[sentiment])
    classification_model.save_model(model_path)



if __name__ == '__main__':
    main()