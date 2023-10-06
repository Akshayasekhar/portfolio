from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # Send an email with the form data
            email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
            recipient_list = ['akshayasekharan21@gmail.com']  # Change to your email address

            send_mail(subject, email_message, email, recipient_list)

            return redirect('/')


# @csrf_exempt
# def details(request):
#     if request.method == 'POST':
#         f_name = request.POST['f_name']
#         l_name = request.POST['l_name']
#         address = request.POST['address']
#         landmark = request.POST['landmark']
#         print(f_name,l_name,address,landmark)
#     return HttpResponse("hello")