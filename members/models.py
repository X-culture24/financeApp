from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

# Custom User Model
class Member(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, default="Unknown")
    last_name = models.CharField(max_length=255, default="Unknown")
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def delete(self, *args, **kwargs):
        self.bills.all().delete()  # Delete all related bills
        if hasattr(self, 'dashboard'):
            self.dashboard.delete()  # Delete the dashboard if it exists
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.email


# Bill model to store bill details
class Bill(models.Model):
    BILL_TYPES = [
        ('WATER', 'Water'),
        ('INTERNET', 'Internet'),
        ('GARBAGE', 'Garbage'),
        ('ELECTRICITY', 'Electricity'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='bills')
    bill_type = models.CharField(max_length=50, choices=BILL_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bill_type} Bill - {self.user.first_name} {self.user.last_name}"

# Dashboard model to display user-specific bill status
class Dashboard(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='dashboard')
    total_bills = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_bills = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    unpaid_bills = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def update_totals(self):
        """Recalculate bill totals."""
        bills = self.user.bills.all()
        self.total_bills = sum(bill.amount for bill in bills)
        self.paid_bills = sum(bill.amount for bill in bills if bill.is_paid)
        self.unpaid_bills = self.total_bills - self.paid_bills
        self.save()

    def __str__(self):
        return f"Dashboard - {self.user.first_name} {self.user.last_name}"
