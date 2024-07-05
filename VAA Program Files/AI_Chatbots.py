import json
import torch
import random
from Neurons import bag_of_words, tokenize, stem
from Brain import NeuralNetwork
from Speaking_Functions import Speak_Os
from nltk.stem.porter import PorterStemmer
from Listening_Functions import Listen_English
from dotenv import load_dotenv
import openai
from Listening_Functions import Listen_English
from Speaking_Functions import Speak_Os

with open("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\Chatbot_Dataset.json",'r') as json_data:
    intents = json.load(json_data)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
FILE = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\Trained_Dataset.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def Chatbot_AI():
    Stemmer = PorterStemmer()
    sentence = Listen_English()
    sentence = str(sentence)
    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)
    _ , predicted = torch.max(output,dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])         
                Speak_Os(reply)
# while 1:
#     Chatbot_AI()


openai.api_key = "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"
load_dotenv()
completion = openai.Completion()

def Chatbot_Open_AI(question, chat_log=None):
    Filelog = open("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\OpenAI_Dataset.txt", "r")
    chat_log_template = Filelog.read()
    Filelog.close()
    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You : {question}\nEMILLY :'
    response = completion.create(model = "text-davinci-002", prompt = prompt, 
    temperature = 0.5, max_tokens = 60, top_p = 0.3, frequency_penalty = 0.5, presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYour Command-:{question} \nEMILLY-:{answer}"
    Filelog = open("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\OpenAI_Dataset.txt", "w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer

# while 1:
#     query = Listen_English()
#     query = str(query)
#     reply = Chatbot_Open_AI(query)
#     Speak_Os(reply)