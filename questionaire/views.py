from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
import os
from django.views.decorators.csrf import csrf_exempt #To allow POST request to a URL


# Read QuestionnairData from file
def read_questionnaire(msg):
    with open("Questionnaire.json") as json_file:
        data = json.load(json_file)
    if msg == 'food':
        return data[0]
    if msg == 'travel':
        return data[1]
    if msg == 'pro':
        return data[2]


# Home page request
def home(request):
    return render(request, 'home.html')


# Contact page request
def contact(request):
    return HttpResponse("<h1> Hi, babe it works!")

def getbot (question):
    print ()


    return answer;

# Question Food
@csrf_exempt
def food_question(request):
    data = read_questionnaire("food")

    f = open("answersFood.txt", "a+")
    f1 = open("answersFood.txt", "r")

    if request.method == 'GET':
        f.write(data['1']['Question'])
        f.write('\n')
        return JsonResponse(data['1'])
    if request.method == 'POST':
        byte_str = request.body
        str_response = byte_str.decode('utf-8')
        json_response = json.loads(str_response)

        if json_response['Question'] == 'Are you hungry. ?':
            if json_response['Answer'] == 'Yes':
                f.write('Yes')
                f.write('\n')
                return JsonResponse(data['2'])
            else:
                json_err = {
                    "Question": "Call me when you are hungry.",
                    "Answer": ""
                }
                f.write('No')
                f.close()
                contents = f1.read()
                print('The answer hierarchy:', contents)
                f1.close()
                os.remove("answersFood.txt")
                return JsonResponse(json_err)

        elif json_response['Question'] == 'What do you want to eat. ?':
            f.write(json_response['Answer'])
            f.write('\n')
            return JsonResponse(data['3'])
        elif json_response['Question'] == 'Would like to add Ketchup. ?':
            if json_response['Answer'] == 'No':
                f.write('No')
                f.write('\n')
                f.close()
                json_err = {
                    "Question": "Your order will be ready without ketchup.",
                    "Answer": ""
                }
                contents = f1.read()
                print('The answer hierarchy:', contents)
                f1.close()
                os.remove("answersFood.txt")
                return JsonResponse(json_err)
            else:
                f.write('Yes')
                f.close()
                json_err = {
                    "Question": "Your order will be ready with ketcup.",
                    "Answer": ""
                }
                contents = f1.read()
                print('The answer hierarchy:', contents)
                f1.close()
                os.remove("answersFood.txt")
                return JsonResponse(json_err)


# Question Travel
@csrf_exempt
def travel_question(request):
    data = read_questionnaire("travel")

    f = open("answersTravel.txt", "a+")
    f1 = open("answersTravel.txt", "r")

    if request.method == 'GET':
        f.write(data['1']['Question'])
        f.write('\n')
        return JsonResponse(data['1'])
    elif request.method == 'POST':
        byte_str = request.body
        str_response = byte_str.decode('utf-8')
        json_response = json.loads(str_response)
        if json_response['Question'] == 'Do you like to travel. ?':
            if json_response['Answer'] == 'Yes':
                f.write('Yes')
                f.write('\n')
                return JsonResponse(data['2'])
            else:
                json_err = {
                    "Question": "Oh, that's very rare to know. ",
                    "Answer": ""
                }
                f.write('No')
                f.close()
                contents = f1.read()
                print('The answer hierarchy:', contents)
                f1.close()
                os.remove("answersTravel.txt")
                return JsonResponse(json_err)
        elif json_response['Question'] == 'What is your favorite travel destination. ?':
            f.write(json_response['Answer'])
            f.write('\n')
            return JsonResponse(data['3'])
        elif json_response['Question'] == 'You prefer traveling with. ?':
            f.write(json_response['Answer'])
            f.write('\n')
            return JsonResponse(data['4'])
        elif json_response['Question'] == 'You travel for. ?':
            json_err = {
                    "Question": "It was nice knowing your travel choices.",
                    "Answer": ""
                }
            f.write(json_response['Answer'])
            f.write('\n')
            f.close()
            contents = f1.read()
            print('The answer hierarchy:', contents)
            f1.close()
            os.remove("answersTravel.txt")
            return JsonResponse(json_err)


# Question Programming
@csrf_exempt
def pro_question(request):
    data = read_questionnaire("pro")

    f = open("answersPro.txt", "a+")
    f1 = open("answersPro.txt", "r")

    if request.method == 'GET':
        f.write(data['1']['Question'])
        f.write('\n')
        return JsonResponse(data['1'])
    elif request.method == 'POST':
        byte_str = request.body
        str_response = byte_str.decode('utf-8')
        json_response = json.loads(str_response)
        if json_response['Question'] == 'Do you like Programming. ?':
            if json_response['Answer'] == 'Yes':
                f.write('Yes')
                f.write('\n')
                return JsonResponse(data['2'])
            else:
                json_err = {
                    "Question": "Well, I'all advice you to learn it. ",
                    "Answer": ""
                }
                f.write('No')
                f.close()
                contents = f1.read()
                print('The answer hierarchy:', contents)
                f1.close()
                os.remove("answersPro.txt")
                return JsonResponse(json_err)
        elif json_response['Question'] == 'Which programming language is your favorite. ?':
            f.write(json_response['Answer'])
            f.write('\n')
            return JsonResponse(data['3'])
        elif json_response['Question'] == 'You like. ?':
            json_err = {
                    "Question": "It was nice knowing your travel choices.",
                    "Answer": ""
                }
            f.write(json_response['Answer'])
            f.write('\n')
            f.close()
            contents = f1.read()
            print('The answer hierarchy:', contents)
            f1.close()
            os.remove("answersPro.txt")
            return JsonResponse(json_err)


# Food page request
def food(request):
    return render(request, 'food.html')


# Travel page request
def travel(request):
    return render(request, 'travel.html')


# Programming page request
def pro(request):
    return render(request, 'pro.html')