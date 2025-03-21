from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL `/` to `/encrypt/`
def redirect_to_encrypt(request):
    return redirect('/encrypt/')

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('encrypt/', include('your_app.urls')),  # Replace 'your_app' with your actual app name
    path('decrypt/', include('your_app.urls')),  # Replace 'your_app' with your actual app name
    path('', redirect_to_encrypt),  # Redirect `/` to `/encrypt/`
]
