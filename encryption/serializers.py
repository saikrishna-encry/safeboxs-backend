from rest_framework import serializers
from .models import EncryptedText

class EncryptedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncryptedText
        fields = ["id", "original_text", "encrypted_text", "created_at"]
