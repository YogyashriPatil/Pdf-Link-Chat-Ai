from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
import mysql.connector

# Sign-in view
from django.views.decorators.csrf import csrf_exempt

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


# Home page view
def home(request):
    return render(request, 'home.html')
