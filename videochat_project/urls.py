from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view here if needed
def home(request):
    return HttpResponse("Welcome to the Homepage")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Homepage directly handled here
    path('call/', include('call.urls')),  # Delegating to call app
]
