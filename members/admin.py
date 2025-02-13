from django.contrib import admin
from .models import Member, Bill, Dashboard

# Register models
admin.site.register(Member)
admin.site.register(Bill)
admin.site.register(Dashboard)

