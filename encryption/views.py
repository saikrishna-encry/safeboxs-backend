from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import socket

def get_client_ip(request):
    """Get the client's IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt  # Disable CSRF for now
def encrypt_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get("text", "")

            if not text:
                return JsonResponse({"error": "No text provided"}, status=400)

            # Simple encryption (reversing text as an example)
            encrypted_text = text[::-1]

            # Store sender IP (mock database)
            request.session['sender_ip'] = get_client_ip(request)

            return JsonResponse({"encrypted_text": encrypted_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def decrypt_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            encrypted_text = data.get("encrypted_text", "")

            if not encrypted_text:
                return JsonResponse({"error": "No encrypted text provided"}, status=400)

            # Decrypt (reverse string back)
            decrypted_text = encrypted_text[::-1]

            # Check if sender and receiver are on the same network
            sender_ip = request.session.get('sender_ip')
            receiver_ip = get_client_ip(request)

            if sender_ip and sender_ip.split('.')[0:3] == receiver_ip.split('.')[0:3]:
                return JsonResponse({"decrypted_text": decrypted_text})
            else:
                return JsonResponse({"error": "Sender and receiver must be on the same network"}, status=403)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
