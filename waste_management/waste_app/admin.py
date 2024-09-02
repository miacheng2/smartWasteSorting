from django.contrib import admin
from .models import User, Waste, DisposalHistory, Bin

admin.site.register(User)
admin.site.register(Waste)
admin.site.register(DisposalHistory)
admin.site.register(Bin)