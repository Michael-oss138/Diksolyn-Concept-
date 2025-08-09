from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Subscribe

# Create your views here.
@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email= data.get("email")

        if not email:
            return JsonResponse({'message': "Email is required"}, status=400)

        if Subscribe.object.filter(email=email).exists():
            return JsonResponse({'message': "Email already subscribed"}, status=400)

        Subscribe.objects.create(email=email)

        send_mail(
            subject = "Welcome to our Updates",
            message = "Thank you for subscribing! We'll keep you updated monthly",
            from_email = "nwaizumicahel0@gmail.com",
            recipient_list = [email],
            fail_silently = False,
        )

        return JsonResponse({'message': "Subscription successful, check your email"})

    return JsonResponse({'message': "Invalid request"}, status=400)
def home(request):
    return render(request, 'tests.html')