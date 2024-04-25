from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Chat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import nltk
import json
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import joblib
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Load the trained model and vectorizer
classifier = joblib.load('mental_health_chatbot_model.joblib')
vectorizer = joblib.load('mental_health_chatbot_vectorizer.joblib')
lemmatizer = WordNetLemmatizer()

with open('intents.json', 'r') as file:
    intents = json.load(file)


def generate_response(user_input):
    # Preprocess user input
    input_vector = vectorizer.transform([lemmatizer.lemmatize(word.lower()) for word in word_tokenize(user_input)])

    # Predict intent
    predicted_label = classifier.predict(input_vector)[0]

    # Retrieve a random response for the predicted intent
    for intent in intents['intents']:
        if intent['tag'] == predicted_label:
            responses = intent['responses']
            return np.random.choice(responses)




    

# Create your views here.
def home(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('login')
    chats = Chat.objects.all()
    if request.method == "POST":
        user_message = request.POST.get("message")
        response = generate_response(user_message)
        Chat.objects.create(user = request.user, message=user_message, response=response)
        return JsonResponse({'message': user_message, 'response': response})
   
    context = {'chats':chats}
    return render(request, 'chat/home.html', context)



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnot exist')
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnot exist')
    context = {'page':page}
    return render(request, 'chat/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    
    if request.method == "POST":
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['username'] and request.POST['email'] and request.POST['password'] and request.POST['password1']:
            username = request.POST['username']
            email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password =  request.POST.get('password')
            password1 =  request.POST.get('password1')
            
            if password == password1:
                if User.objects.filter(username = username).exists():
                    messages.error(request,'username already taken')
                    return redirect('register')
                
                elif User.objects.filter(email = email).exists():
                    messages.error(request,'email already taken')
                    return redirect('register')
                
                else :
                    user = User.objects.create_user(username=username,password=password,email=email, first_name=firstname, last_name =lastname)   
                    user.save()
                    login(request, user)
                    return redirect('home')
            
            else:
                messages.info(request,'password not matching, please try again')
                return redirect('register')

    return render(request, 'chat/login_register.html')


    
