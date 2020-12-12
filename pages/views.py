from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date')
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'teams':teams,
        'featured_cars': featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'year_search':year_search,
        'city_search':city_search,
        'body_style_search':body_style_search,
    }
    return render(request,'home.html',data)
def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'about.html',data)
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'adityaparashar863@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    
    return render(request,'contact.html')

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'dashboard.html', data)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')
    
    return render(request,'login.html')
def services(request):
    return render(request,'services.html')
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')