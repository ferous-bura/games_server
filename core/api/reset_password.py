# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
import json


@csrf_exempt
def reset_password(request, uidb64, token):
    if request.method == "POST":
        data = json.loads(request.body)
        new_password = data.get("new_password")

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return JsonResponse({"message": "Password reset successfully."})
        else:
            return JsonResponse({"message": "Invalid reset link."}, status=400)

    return JsonResponse({"message": "Invalid request method."}, status=405)
