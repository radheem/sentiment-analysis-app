from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import torch

class sentimentAnalysis:
    def __init__(self,model_name, model_path="",is_local=False):
        self.model_path = model_path
        self.model_name = model_name
        self.model = self.__get_model(is_local)
        self.tokenizer = self.__get_tokenizer()
        self.config = self.__get_config()
        
    def __get_model(self,is_local):
        if is_local:
            return torch.load(self.model_path)
        else:
            return AutoModelForSequenceClassification.from_pretrained(self.model_name)

    def __get_tokenizer(self):
        return AutoTokenizer.from_pretrained(self.model_name)

    def __get_config(self):
        return AutoConfig.from_pretrained(self.model_name)

    def preprocess(self,text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    def get_sentiment(self,text) -> str:
        ptext = self.preprocess(text)
        encoded_input = self.tokenizer(ptext, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        return self.config.id2label[ranking[0]]    

    def save_model(self,model_path):
        torch.save(self.model, model_path)