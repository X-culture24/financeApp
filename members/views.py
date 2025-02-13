from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from decimal import Decimal

from .models import Member, Bill, Dashboard
from .forms import MemberCreationForm  # Import the custom registration form
from django.urls import reverse

# Homepage View (Landing Page)
def home(request):
    return render(request, 'main.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Dashboard.objects.create(user=user)  # Create a Dashboard for the new user
            login(request, user)  # Auto-login after registration
            return redirect('dashboard')
    else:
        form = MemberCreationForm()
    
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use `.get()` to avoid KeyError
        password = request.POST.get('password')
        next_url = request.GET.get('next', 'dashboard')  # Get 'next' parameter or default to 'dashboard'

        if not email or not password:
            return render(request, 'login.html', {'error': 'Email and password are required'})

        user = authenticate(request, email=email, password=password)  # Authenticate using email

        if user is not None:
            login(request, user)
            return redirect(reverse(next_url))  # Ensure next_url is valid
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')
# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# Dashboard View
@login_required
def dashboard(request):
    user = request.user
    dashboard, _ = Dashboard.objects.get_or_create(user=user)
    bills = Bill.objects.filter(user=user)
    
    # Ensure `update_totals` method exists in the Dashboard model
    if hasattr(dashboard, 'update_totals'):
        dashboard.update_totals()

    context = {
        'user': user,
        'dashboard': dashboard,
        'bills': bills,
    }
    return render(request, 'dashboard.html', context)

# Add Bill View
@login_required
def add_bill(request):
    if request.method == 'POST':
        bill_type = request.POST.get('bill_type')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')
        is_paid = request.POST.get('is_paid') == 'on'

        try:
            amount = Decimal(amount)
        except (ValueError, TypeError):
            return render(request, 'add_bill.html', {'error': 'Invalid amount'})

        Bill.objects.create(
            user=request.user,
            bill_type=bill_type,
            amount=amount,
            due_date=due_date,
            is_paid=is_paid
        )
        return redirect('dashboard')
    
    return render(request, 'add_bill.html')

# Mark Bill as Paid View
@login_required
def mark_paid(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id, user=request.user)
    bill.is_paid = True
    bill.save()
    return redirect('dashboard')
