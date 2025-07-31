from rest_framework import serializers
from apps.app2.Models.models import ImageModel
import mimetypes

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'image', 'uploaded_at']

    def validate_image(self, value):
        if value.size > 5 * 1024 * 1024:  # 5MB limit
            raise serializers.ValidationError("Image file too large. Maximum size is 5MB.")
        mime_type, _ = mimetypes.guess_type(value.name)
        if mime_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise serializers.ValidationError("Invalid file type. Only JPG, JPEG, and PNG are allowed.")
        return value