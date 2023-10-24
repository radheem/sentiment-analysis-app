from django.shortcuts import render, redirect
from .roberta_base_app import sentimentAnalysis
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import Classify
import logging
from .models import UserClassifications

import os 
load_dotenv()
model_name  = str(os.getenv('SENTIMENT_MODEL_NAME'))
model_path = str(os.getenv('SENTIMENT_MODEL_PATH'))
classification_model = sentimentAnalysis(model_name,model_path,True) 

@login_required
def history(request):
    user_id = request.user.id
    records = UserClassifications.objects.filter(user_id=user_id).order_by('-createdAt')[:50]
    return render(request, 'classification_history.html',{"records":records})

@login_required
def classification(request):
    context = {}
    context["form"] = Classify()
    if request.method == 'POST':
        input_text = Classify(request.POST)
        if input_text.is_valid():
            input_data = input_text.cleaned_data['text']
            sentiment = classification_model.get_sentiment(input_data)
            input_text.sentiment = sentiment
            context["form"] = input_text
            context["sentiment"] = sentiment
            record  = UserClassifications.objects.create(user_id=request.user.id,
                                          user_name=request.user.username,
                                          input_text=input_data,
                                          sentiment=sentiment)
            return render(request, 'classify.html',context)
        else:
            logging.log(logging.INFO,"Invalid form: {}".format(request.POST))
            return HttpResponse("Invalid form")
    else:
        return render(request, 'classify.html',context)

@login_required
def delete_record(request, id):  
    employee = UserClassifications.objects.get(id=id)  
    employee.delete()  
    return redirect("history")  