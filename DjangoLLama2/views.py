from django.shortcuts import render
from django.http import HttpResponse
from .models import *

#importing the langchain and llama2 related functions
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import LlamaCpp
from llama_cpp import Llama
#loading the model at the start of the server itself

def home(request):
    return render(request, "home.html")

def getAnswer(request):

    model_path="DjangoLLama2/llama-2-7b-chat.ggmlv3.q8_0.bin"
    print(request.GET['question'])
    llm = Llama(model_path=model_path)
    
    query = request.GET['question']

    
    
    model_out = llm(query, 
        max_tokens=4000, 
        echo=True)

    output = model_out['choices'][0]['text']

    model = LLamaQA(
        question = query,
        answer =output
    )
    model.save()

    return render(request, 'home.html', {'answer': output})
