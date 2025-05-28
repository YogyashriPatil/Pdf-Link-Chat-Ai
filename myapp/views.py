from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import mysql.connector
from django.contrib.auth import logout
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from google.genai import Client
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import google as genai
from google.genai import Client

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        useremail = request.POST.get('signin-email')
        passw = request.POST.get('signin-password')

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="wtl_project",
        )

        mycur=mydb.cursor()
        mycur.execute("select * from usermast where uemail='"+useremail+"' and upass='"+passw+"' ;")

        mydata=mycur.fetchone()
        if mydata is not None:
            # return redirect('home')
            return render(request,'home.html')
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')


# Sign-up view
def signup(request):
    if request.method == "POST":
        name = request.POST.get("signup-name")
        email = request.POST.get("signup-email")
        password = request.POST.get("signup-password")
        repassword = request.POST.get("signup-repassword")

        if password != repassword:
            return HttpResponse("<h1>Passwords do not match.</h1>")

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="wtl_project",
            )
            mycur = mydb.cursor()

            # ✅ Secure way to insert data (prevents SQL injection)
            mycur.execute(
                "INSERT INTO usermast(uname, uemail, upass) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            mydb.commit()
            mycur.close()
            mydb.close()

            messages.success(request, "Sign-up successful. Please sign in.")
            return redirect('signin')  # Redirect to signin after success
        except mysql.connector.Error as err:
            return HttpResponse(f"<h1>Database Error: {err}</h1>")

    return render(request, 'signup.html')

def custom_logout(request):
    logout(request)
    return redirect('signin')

from django.http import JsonResponse

def chattoai(request):
    client = Client(api_key="AIzaSyDRy36UNei42DJEJdwaBzj9lOh3-5rFGUM")
    system_prompt = """
        Your an AI assistant whose work on the simple message of user.
        and you give the user friendly message.
        And the also 
    """
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[
                system_prompt,
                user_input
            ],
        )
        # Return a dictionary with a key and the AI response text as value
        return JsonResponse({"response": response.text})
    return render(request, "chattoai.html")



def chattopdf(request):
    return render(request, "chattopdf.html")


def builtownai(request):
    
    client=Client(api_key="AIzaSyDRy36UNei42DJEJdwaBzj9lOh3-5rFGUM")
    system_prompt=request.POST.get('first_message')

    if request.method == "POST":
        user_input = request.POST.get("message", "")
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=[
                system_prompt,
                user_input
            ],
        )
        response = {"response": f"{response.text}"}
        return JsonResponse(response)
    return render(request, "builtownai.html")

def home(request):
    return render(request, 'home.html')

def setting(request):
    return render(request, 'setting.html')
