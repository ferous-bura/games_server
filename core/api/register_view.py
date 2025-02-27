import json
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from games_server.settings import DEFAULT_FROM_EMAIL

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already exists."}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email already exists."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False  # User is inactive until email confirmation
        user.save()

        # Send confirmation email
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_url = f"http://127.0.0.1:8000/api/confirm-email/{uid}/{token}/"

        subject = "Confirm your email"
        message = render_to_string('core/email_confirmation.html', {
            'user': user,
            'confirm_url': confirm_url,
        })
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [email])

        return JsonResponse({"success": True, "message": "Registration successful. Please check your email to confirm your account."})

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)

